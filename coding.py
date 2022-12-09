from flask import *
from DBConnection import Db
app=Flask(__name__)
app.secret_key="ghhjggm"





@app.route('/')
def login():
    return render_template("login.html")



@app.route('/login_post',methods=['post'])
def login_post():
    uname = request.form['textfield']
    passwrd = request.form['textfield2']
    db=Db()
    qry="select * from login where username='"+uname+"' and password='"+passwrd+"'"
    res=db.selectOne(qry)
    print(res)
    if res is not None:
        session['lid']=res['lid']
        if res['type']=='admin':
            return redirect('/Home')
        elif res['type']=='manufacture':
            return redirect('/Home_Manufactors')
        else:
            return "ok"
    else:
        return "okk"




#-----------------------------admin






@app.route('/Home')
def Home():
    return render_template("Admin/Home.html")





@app.route('/approved_manufactures')
def approved_manufactures():
    db=Db()
    qry="SELECT * FROM manufacturer  where status='Approved'"
    res=db.select(qry)
    return render_template("Admin/Approved Manufactures.html",data=res)


@app.route('/approved_manufactures_post',methods=['post'])
def approved_manufactures_post():
    name=request.form['textfield']
    db = Db()
    qry = "SELECT * FROM manufacturer  where status='approved' AND name LIKE '%"+name+"%'"
    res = db.select(qry)
    return render_template("Admin/Approved Manufactures.html",data=res)






@app.route('/Change_password')
def Change_password():
    return render_template("Admin/ChangePassword.html")


@app.route('/Change_passwor_post',methods=['post'])
def Change_passwor_post():
    current_pass = request.form['textfield']
    new_pass = request.form['textfield2']
    confirm_pass = request.form['textfield3']
    return render_template("Admin/ChangePassword.html")






@app.route('/new_complaint')
def new_complaint():
    db = Db()
    qry = "SELECT * FROM compalint JOIN USER ON user.user_lid = compalint.user_lid"
    res = db.select(qry)
    return render_template("Admin/NewComplaint.html",data=res)


@app.route('/new_complaint_post',methods=['post'])
def new_complaint_post():
    pro_name = request.form['textfield']
    return render_template("Admin/NewComplaint.html")






@app.route('/replay/<id>')
def replay(id):
    return render_template("Admin/Replay.html",rid=id)



@app.route('/replay_post',methods=['post'])
def replay_post():
    comp_id=request.form['comp_id']
    reply = request.form['textarea']
    db=Db()
    qry="UPDATE `compalint` SET replay='"+reply+"',STATUS='replyed' WHERE comp_id="+comp_id+""
    res=db.update(qry)
    return render_template("Admin/Replay.html",data=res)






@app.route('/verifing_manufactiores')
def verifing_manufactiores():
    db = Db()
    qry = "SELECT * FROM manufacturer where status= 'pending' "
    res = db.select(qry)
    return render_template("Admin/VerifingManufactores.html",data=res)



@app.route('/approve_manufactiores/<id>')
def approve_manufactiores(id):
    qry="UPDATE `manufacturer` SET STATUS='approved' WHERE man_id='"+id+"'"
    db=Db()
    res=db.update(qry)
    return '''<script>alert('approved successfully');window.location='/verifing_manufactiores'</script>'''



@app.route('/reject_manufactiores/<id>')
def reject_manufactiores(id):
    qry="UPDATE `manufacturer` SET STATUS='reject' WHERE man_id='"+id+"'"
    db=Db()
    res=db.update(qry)
    return '''<script>alert('Rejected Successfully');window.location='/verifing_manufactiores'</script>'''




@app.route('/verifing_manufactiores_post',methods=['post'])
def verifing_manufactiores_post():
    name = request.form['textfield']
    db=Db()
    qry=" SELECT * FROM manufacturer  WHERE STATUS='pending' AND NAME LIKE '%"+name+"%' "
    res=db.select(qry)
    return render_template("Admin/VerifingManufactores.html",data=res)






@app.route('/view_user')
def view_user():
    db = Db()
    qry = "SELECT * FROM user "
    res = db.select(qry)
    return render_template("Admin/ViewUser.html",data=res)



@app.route('/view_user_post',methods=['post'])
def view_user_post():
    name = request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `user`  WHERE naame LIKE '%"+name+"%' "
    res = db.select(qry)
    return render_template("Admin/ViewUser.html",data=res)





#-------------------------------------------------------------manufacters


@app.route('/catagory_managment')
def catagory_managment():
    db = Db()
    qry = "SELECT * FROM category where `man_lid`='"+str(session['lid'])+"'"
    res = db.select(qry)
    return render_template("Manufacters/CatagoryManagment.html",data=res)


@app.route('/catagory_managment_post',methods=['post'])
def catagory_managment_post():
    name = request.form['textfield']
    db = Db()
    qry = " SELECT * FROM category where `man_lid`='"+str(session['lid'])+"' and `category` LIKE '"+name+"' "
    res = db.select(qry)
    return render_template("Manufacters/CatagoryManagment.html",data=res)




@app.route('/Catagory_Managment_Add')
def Catagory_Managment_Add():
    return render_template('Manufacters/Catagory Managment Add.html')


@app.route('/Catagory_Managment_Add_post',methods=['post'])
def Catagory_Managment_Add_post():
    CataName = request.form['textfield']
    db = Db()
    qry = "INSERT INTO category(`category`,man_lid )VALUES('"+CataName+"','"+str(session['lid'])+"')"
    res = db.insert(qry)
    return redirect('/catagory_managment')




@app.route('/catagory_managment_delete/<id>')
def catagory_managment_add(id):
    db = Db()
    qry = "DELETE FROM `category` WHERE `category-id` ='"+id+"'"
    res = db.delete(qry)
    return "<script>alert('deleted');window.location='/catagory_managment'</script>"




@app.route('/Catagory_Managment_edit/<id>')
def Catagory_Managment_edit(id):
    db = Db()
    qry = " select * from category WHERE  `category-id`= '"+id+"'"
    res = db.selectOne(qry)
    return render_template('Manufacters/Catagory Managment Edit.html',data=res)


@app.route('/Catagory_Managment_edit_post',methods=['post'])
def Catagory_Managment_edit_post():
    CataName = request.form['textfield']
    Id = request.form['id']
    db = Db()
    qry = " UPDATE `category` SET `category`='"+CataName+"' WHERE `category-id`='"+Id+"' "
    res = db.update(qry)
    return '''<script>alert("updated");window.location='/catagory_managment'</script>'''






@app.route('/delivary_rating')
def delivary_rating():
    db = Db()
    # qry = "SELECT * FROM delivery_rating " \
    #       "JOIN `deliverry_assign` ON `deliverry_assign`.`assign_id`=`delivery_rating`.`assign_id`" \
    #       "JOIN `order_main`ON `order_main`.`order_id`=`deliverry_assign`.`order_id`JOIN `user` ON `user`.`user_lid`=`order_main`.`user-lid`" \
    #       "JOIN `staff` ON `staff`.`staff-lid`=`deliverry_assign`.`staff_id` WHERE `order_main`.`order_id`=''  "
    qry="SELECT * FROM delivery_rating JOIN `deliverry_assign` ON `deliverry_assign`.`assign_id`=`delivery_rating`.`assign_id` JOIN `order_main`ON `order_main`.`order_id`=`deliverry_assign`.`order_id`JOIN `user` ON `user`.`user_lid`=`order_main`.`user-lid` JOIN `staff` ON `staff`.`staff-lid`=`deliverry_assign`.`staff_id` WHERE `order_main`.`order_id`='"+str(session['lid'])+"'"
    res = db.select(qry)
    return render_template("Manufacters/DelivaryRating.html",data=res)






@app.route('/product_managment')
def product_managment():
    db = Db()
    qry = "SELECT * FROM `product` JOIN `category`ON `category`.`category-id`=`product`.`categort-id` WHERE `man_id`='"+str(session['lid'])+"' "
    res = db.select(qry)
    return render_template("Manufacters/ProductManagment.html",data=res)




@app.route('/product_managment_post',methods=['post'])
def product_managment_post():
    pro_name = request.form['textfield']
    db = Db()
    qry = " SELECT * FROM `product`JOIN `category`ON `category`.`category-id`=`product`.`categort-id` WHERE `man_id`='"+str(session['lid'])+"' and `product_name`= '"+pro_name+"'  "
    res = db.select(qry)
    return render_template("Manufacters/ProductManagment.html",data = res)




@app.route('/Product_Managment_edit/<id>')
def Product_Managment_edit(id):
    db = Db()
    qry="SELECT * FROM `category`"
    res=db.select(qry)
    qry2 = "SELECT * FROM `product`  JOIN `category`ON `category`.`category-id`=`product`.`categort-id` WHERE `pid`='"+id+"'"
    res1=db.selectOne(qry2)
    return render_template("Manufacters/ProductManagment-Edit.html",data=res1,data2=res)




@app.route('/Product_Managment_edit_post',methods=['post'])
def Product_Managment_edit_post():
    Id = request.form['id']
    img = request.files['fileField']
    pro_name = request.form['textfield']
    catgry = request.form['textfield2']
    price = request.form['textfield3']
    qty = request.form['textfield4']
    discr = request.form['textarea']
    from _datetime import datetime
    date = datetime.now().strftime("%d%M%y-%H%M%S")
    img.save("C:\\Users\\vishn\\PycharmProjects\\digit dimes\\static\\product\\" + date + ".jpg")
    path = "/static/product/" + date + ".jpg"
    db = Db()
    qry = " UPDATE `product` SET `photo`='"+path+"',`product_name`='"+pro_name+"',`price`='"+str(price)+"',`qty`='"+str(qty)+"',`categort-id`='"+catgry+"',`description`='"+discr+"' WHERE `pid`='"+Id+"' "
    res = db.update(qry)
    return redirect('/product_managment')





@app.route('/product_managment_addnew')
def product_managment_addnew():
    db = Db()
    qry = " select * from category WHERE man_lid='"+str(session['lid'])+"'  "
    res = db.select(qry)

    return render_template("Manufacters/Product managment-Add new.html",data = res)




@app.route('/product_managment_addnew_post',methods=['post'])
def product_managment_addnew_post():
    imge = request.files['fileField']
    Pname = request.form['textfield']
    Ctgry = request.form['textfield2']
    price = request.form['textfield3']
    qty = request.form['textfield4']
    description = request.form['textarea']
    from _datetime import datetime
    date=datetime.now().strftime("%d%M%y-%H%M%S")
    imge.save("C:\\Users\\vishn\\PycharmProjects\\digit dimes\\static\\product\\"+date+".jpg")
    path="/static/product/"+date+".jpg"
    db = Db()
    qry = " INSERT INTO `product` (`photo`,`product_name`,`description`,`price`,`qty`,`categort-id`,`man_id`)VALUES('"+path+"','"+Pname +"','"+description+"','"+str(price)+"','"+ str(qty)+"','"+Ctgry+"','"+str(session['lid'])+"' ) "
    res = db.insert(qry)
    return redirect('/product_managment')



@app.route('/product_managment_delete/<id>')
def product_managment_delete(id):
    db = Db()
    qry = " DELETE FROM `product` WHERE `pid`='"+id+"' "
    res = db.delete(qry)
    return "<script>alert('deleted');window.location='/product_managment'</script>"






@app.route('/product_review')
def product_review():
    return render_template("Manufacters/ProductReview.html")






@app.route('/profile_managment')
def profile_managment():
    return render_template("Manufacters/ProfileManagment.html")




@app.route('/profile_managment_post',methods=['post'])
def profile_managment_post():
    name = request.form['textfield']
    propri_name = request.form['textfield2']
    ph = request.form['textfield3']
    ema =  request.form['textfield4']
    return render_template("Manufacters/ProfileManagment.html")






@app.route('/sign_up')
def sign_up():
    return render_template("Manufacters/Signup.html")



@app.route('/sign_up_post',methods=['post'])
def sign_up_post():
    usrname  = request.form['textfield']
    propri_name  = request.form['textfield2']
    ph = request.form['textfield3']
    ema  = request.form['textfield4']
    place  = request.form['textfield5']
    pst  = request.form['textfield6']
    pin  = request.form['textfield7']
    Latitude = request.form['textfield8']
    Longitude = request.form['textfield9']
    passwd = request.form['textfield10']
    passwdC = request.form['textfield11']
    db=Db()
    if passwd==passwdC:
        qry="INSERT INTO `login`(`username`,`password`,`type`)VALUES('"+ema+"','"+passwd+"','manufacture')"
        res=db.insert(qry)
        qry2="INSERT INTO `manufacturer` (`man_lid`,`name`,`propreitir_name`,`email`,`phone`,`place`,`post`,`pin`,`latitude`,`longitude`,`status`) VALUES('"+str(res)+"','"+usrname+"','"+propri_name+"','"+ph+"','"+ema+"','"+place+"','"+pst+"','"+pin+"','"+Latitude+"','"+Longitude+"','pending')"
        res=db.insert(qry2)
        return redirect('/')
    else:
        "ok"






@app.route('/staff_managment')
def staff_managment():
    db= Db()
    qry = "SELECT * FROM `staff` WHERE `man-id`= '"+str(session['lid'])+"' "
    res = db.select(qry)
    return render_template("Manufacters/StaffManagment-0.html",data=res)


@app.route('/staff_managment_post',methods=['post'])
def staff_managment_post():
    Search = request.form['textfield']
    db=Db()
    qry="SELECT * FROM `staff` WHERE `man-id`='"+str(session['lid'])+"' and sname like '"+Search+"'"
    res=db.select(qry)
    return render_template("Manufacters/StaffManagment-0.html",data=res)




@app.route('/staff_managment_add')
def staff_managment_add():
    return render_template("Manufacters/StaffManagment-AddNew.html")


@app.route('/staff_managment_add_post',methods=['post'])
def staff_managment_add_post():
    Gender= request.form['checkbox']
    Name = request.form['textfield']
    age = request.form['textfield2']
    phone = request.form['textfield3']
    ema = request.form['textfield4']
    place = request.form['textfield5']
    pin = request.form['textfield6']
    Post = request.form['textfield7']
    city = request.form['textfield8']
    db=Db()
    qry = "INSERT INTO `login`(`username`,`password`,`type`)VALUES('"+ema+"','"+phone+"','staff')"
    res=db.insert(qry)
    qry2 = "INSERT INTO `staff`(`staff-lid`,`man-id`,`sname`,`age`,`gender`,`place`,`post`,`pin`,`city`,`phone`,`email`) VALUES('"+str(res)+"','"+str(session['lid'])+"','"+Name+"','"+age+"','"+Gender+"','"+place+"','"+Post+"','"+pin+"','"+city+"','"+phone+"','"+ema+"')"
    res=db.insert(qry2)
    return redirect('/staff_managment')






@app.route('/StaffManagment_Edit/<id>')
def StaffManagment_Edit(id):
    db = Db()
    qry = "Select * from staff where staff_='"+id+"'"
    res = db.selectOne(qry)
    return render_template("Manufacters/StaffManagment-Edit.html",data=res)



@app.route('/StaffManagment_Edit_post',methods=['post'])
def StaffManagment_Edit_post():
    Id = request.form['ID']
    Gender = request.form['radio']
    Name = request.form['textfield']
    age = request.form['textfield2']
    phone = request.form['textfield3']
    ema = request.form['textfield4']
    place = request.form['textfield5']
    pin = request.form['textfield6']
    Post = request.form['textfield7']
    city = request.form['textfield8']
    db = Db()
    qry = " UPDATE `staff` SET `sname`='"+Name+"' ,`age`='"+age+"' ,`gender`='"+Gender+"' ,`place`='"+place+"',`post`='"+Post+"',`pin`='"+pin+"',`city`='"+city+"',`phone`='"+phone+"',`email`='"+ema+"' WHERE staff_='"+Id+"'"
    res = db.update(qry)
    return redirect('/staff_managment')




@app.route('/Staff_management_Delete/<id>')
def Staff_management_Delete(id):
    db = Db()
    qry = "DELETE FROM `staff` WHERE `staff_`='"+id+"'"
    res = db.delete(qry)
    return "<script>alert('deleted');window.location='/staff_managment'</script>"






@app.route('/Home_Manufactors')
def Home_Manufactors():
    return render_template("Manufacters/Home_Manufactors.html")




app.run(debug=True)