from flask import *
from DBConnection import Db
app=Flask(__name__)
app.secret_key="ghhjggm"



#-----------------------------------------------------------------------------------------------------------------------Login

@app.route('/')
def login():
    return render_template("LoginPage.html")

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
        session['log']="lin"
        if res['type']=='admin':
            return redirect('/Home')
        elif res['type']=='manufacture':
            return redirect('/Home_Manufactors')
        else:
            return "<script>alert('please check your login credentials');window.location='/'</script>"
    else:
        return "<script>alert('please check your login credentials');window.location='/'</script>"



#=======================================================================================================================
#--------------------------------------------------------------admin----------------------------------------------------
#=======================================================================================================================


@app.route('/logout')
def logout():
    session['log']==""
    return render_template("LoginPage.html")



@app.route('/Home')
def Home():
    if session['log']=='lin':
        return render_template("Admin/HomePage.html")
    else:
        return "<script>alert('Log out');window.location='/'</script>"





@app.route('/approved_manufactures')
def approved_manufactures():
    db=Db()
    qry="SELECT * FROM manufacturer  where status='Approved'"
    res=db.select(qry)
    if session['log'] == 'lin':
        return render_template("Admin/Approved Manufactures.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"


@app.route('/approved_manufactures_post',methods=['post'])
def approved_manufactures_post():
    name=request.form['textfield']
    db = Db()
    qry = "SELECT * FROM manufacturer  where status='approved' AND name LIKE '%"+name+"%'"
    res = db.select(qry)
    return render_template("Admin/Approved Manufactures.html",data=res)






@app.route('/Change_password')
def Change_password():
    if session['log'] == 'lin':
       return render_template("Admin/ChangePassword.html")
    else:
        return "<script>alert('Log out');window.location='/'</script>"



@app.route('/Change_passwor_post',methods=['post'])
def Change_passwor_post():
    current_pass = request.form['textfield']
    new_pass = request.form['textfield2']
    confirm_pass = request.form['textfield3']
    db = Db()
    qry="select * from login where password='"+current_pass+"' and lid='"+str(session['lid'])+"'"
    res=db.selectOne(qry)
    if res is not None:
        if new_pass==confirm_pass:
            qry1=" UPDATE `login` SET `password`='"+new_pass+"' WHERE `lid`='"+str(session['lid'])+"'"
            res=db.update(qry1)
    return '''<script>alert('Password changed Successfully');window.location='/Home'</script>'''






@app.route('/new_complaint')
def new_complaint():
    db = Db()
    qry = "SELECT * FROM compalint JOIN USER ON user.user_lid = compalint.user_lid"
    res = db.select(qry)
    if session['log'] == 'lin':
       return render_template("Admin/NewComplaint.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"



@app.route('/new_complaint_post',methods=['post'])
def new_complaint_post():
    pro_name = request.form['textfield']
    return render_template("Admin/NewComplaint.html")






@app.route('/replay/<id>')
def replay(id):
    if session['log'] == 'lin':
       return render_template("Admin/Replay.html",rid=id)
    else:
        return "<script>alert('Log out');window.location='/'</script>"




@app.route('/replay_post',methods=['post'])
def replay_post():
    comp_id=request.form['comp_id']
    reply = request.form['textarea']
    db=Db()
    qry="UPDATE `compalint` SET replay='"+reply+"',STATUS='replyed' WHERE comp_id='"+comp_id+"'"
    res=db.update(qry)
    return redirect("/new_complaint")






@app.route('/approve_manufactiores/<id>/<ema>/<passwd>')
def approve_manufactiores(id,ema,passwd):
    db = Db()
    qry2 = "INSERT INTO `login`(`username`,`password`,`type`)VALUES('" + ema + "','" + passwd + "','manufacture')"
    res2 = db.insert(qry2)
    qry="UPDATE `manufacturer` SET STATUS='approved',`man_lid`='"+str(res2)+"' WHERE man_id='"+id+"'"
    res=db.update(qry)
    if session['log'] == 'lin':
        return '''<script>alert('approved successfully');window.location='/verifing_manufactiores'</script>'''
        pass
    else:
        pass
    return "<script>alert('Log out');window.location='/'</script>"




@app.route('/verifing_manufactiores')
def verifing_manufactiores():
    db = Db()
    qry = "SELECT * FROM manufacturer where status= 'pending' "
    res = db.select(qry)
    if session['log'] == 'lin':
      return render_template("Admin/VerifingManufactores.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"



@app.route('/reject_manufactiores/<id>/<man_lid>')
def reject_manufactiores(id,man_lid):
    db = Db()
    qry ="UPDATE `manufacturer` SET STATUS='reject' WHERE man_id='"+id+"'"
    res = db.update(qry)
    print(man_lid)
    qry2 = " DELETE FROM `login` WHERE lid='"+man_lid+"'"
    res2 = db.update(qry2)
    if session['log'] == 'lin':
       return '''<script>alert('Rejected Successfully');window.location='/verifing_manufactiores'</script>'''
    else:
        return "<script>alert('Log out');window.location='/'</script>"




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
    if session['log'] == 'lin':
       return render_template("Admin/ViewUser.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"



@app.route('/view_user_post',methods=['post'])
def view_user_post():
    name = request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `user`  WHERE naame LIKE '%"+name+"%' "
    res = db.select(qry)
    return render_template("Admin/ViewUser.html",data=res)






#=======================================================================================================================
#-------------------------------------------------------------- manufacteres -------------------------------------------
#=======================================================================================================================



@app.route('/catagory_managment')
def catagory_managment():
    db = Db()
    qry = "SELECT * FROM category where `man_lid`='"+str(session['lid'])+"'"
    res = db.select(qry)
    if session['log'] == 'lin':
      return render_template("Manufacters/CatagoryManagment.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"




@app.route('/catagory_managment_post',methods=['post'])
def catagory_managment_post():
    name = request.form['textfield']
    db = Db()
    qry = " SELECT * FROM category where `man_lid`='"+str(session['lid'])+"' and `category` LIKE '"+name+"' "
    res = db.select(qry)
    return render_template("Manufacters/CatagoryManagment.html",data=res)




@app.route('/Catagory_Managment_Add')
def Catagory_Managment_Add():
    if session['log'] == 'lin':
       return render_template('Manufacters/Catagory Managment Add.html')
    else:
        return "<script>alert('Log out');window.location='/'</script>"


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
    if session['log'] == 'lin':
       return "<script>alert('deleted');window.location='/catagory_managment'</script>"
    else:
        return "<script>alert('Log out');window.location='/'</script>"




@app.route('/Catagory_Managment_edit/<id>')
def Catagory_Managment_edit(id):
    db = Db()
    qry = " select * from category WHERE  `category-id`= '"+id+"'"
    res = db.selectOne(qry)
    if session['log'] == 'lin':
       return render_template('Manufacters/Catagory Managment Edit.html',data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"



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
    qry=" SELECT * FROM `delivery_rating` JOIN `deliverry_assign`ON`deliverry_assign`.`assign_id`=`delivery_rating`.`assign_id` JOIN `order_main`ON`order_main`.`order_id`=`deliverry_assign`.`order_id`JOIN `user`ON`user`.`user_lid`=`order_main`.`user-lid`JOIN `staff`ON `staff`.`staff_`=`deliverry_assign`.`staff_id`WHERE `staff`.`man-id`='"+str(session['lid'])+"' "
    res = db.select(qry)
    if session['log'] == 'lin':
       return render_template("Manufacters/DelivaryRating.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"






@app.route('/product_managment')
def product_managment():
    db = Db()
    qry = "SELECT * FROM `product` JOIN `category`ON `category`.`category-id`=`product`.`categort-id` WHERE `man_id`='"+str(session['lid'])+"' "
    res = db.select(qry)
    if session['log'] == 'lin':
       return render_template("Manufacters/ProductManagment.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"




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
    if session['log'] == 'lin':
       return render_template("Manufacters/ProductManagment-Edit.html",data=res1,data2=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"




@app.route('/Product_Managment_edit_post',methods=['post'])
def Product_Managment_edit_post():
    Id = request.form['id']
    img = request.files['fileField']
    pro_name = request.form['textfield']
    catgry = request.form['textfield2']
    price = request.form['textfield3']
    qty = request.form['textfield4']
    discr = request.form['textarea']

    db=Db()
    if img.filename != '':
        from _datetime import datetime
        date = datetime.now().strftime("%d%M%y-%H%M%S")
        img.save("C:\\Users\\vishn\\PycharmProjects\\digit dimes\\static\\product\\" + date + ".jpg")
        path = "/static/product/" + date + ".jpg"
        qry = " UPDATE `product` SET `photo`='"+path+"',`product_name`='"+pro_name+"',`price`='"+str(price)+"',`qty`='"+str(qty)+"',`categort-id`='"+catgry+"',`description`='"+discr+"' WHERE `pid`='"+Id+"' "
        res = db.update(qry)
    else:
        qry = " UPDATE `product` SET `product_name`='" + pro_name + "',`price`='" + str(
            price) + "',`qty`='" + str(
            qty) + "',`categort-id`='" + catgry + "',`description`='" + discr + "' WHERE `pid`='" + Id + "' "
        res = db.update(qry)
    return redirect('/product_managment')





@app.route('/product_managment_addnew')
def product_managment_addnew():
    db = Db()
    qry = " select * from category WHERE man_lid='"+str(session['lid'])+"'  "
    res = db.select(qry)
    if session['log'] == 'lin':
       return render_template("Manufacters/Product managment-Add new.html",data = res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"




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
    if session['log'] == 'lin':
       return "<script>alert('deleted');window.location='/product_managment'</script>"
    else:
        return "<script>alert('Log out');window.location='/'</script>"






@app.route('/product_review')
def product_review():
    db = Db()
    qry = " SELECT * FROM `product_review` JOIN `user`ON `user`.`user_lid`=`product_review`.`user_lid` JOIN `product`ON`product`.`pid` = `product_review`.`pid` WHERE `product`.`man_id`= '"+str(session['lid'])+"' "
    res = db.select(qry)
    if session['log'] == 'lin':
       return render_template("Manufacters/ProductReview.html",data = res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"






@app.route('/profile_managment')
def profile_managment():
    db = Db()
    qry = "    SELECT * FROM `manufacturer` WHERE `man_lid`='"+str(session['lid'])+"'  "
    res = db.selectOne(qry)
    if session['log'] == 'lin':
       return render_template("Manufacters/ProfileManagment.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"




@app.route('/profile_managment_post',methods=['post'])
def profile_managment_post():
    usrname = request.form['textfield']
    propri_name = request.form['textfield2']
    ph = request.form['textfield3']
    ema = request.form['textfield4']
    place = request.form['textfield5']
    pst = request.form['textfield6']
    pin = request.form['textfield7']
    Latitude = request.form['textfield8']
    Longitude = request.form['textfield9']
    db = Db()
    qry = "  UPDATE `manufacturer` SET `name`='"+usrname+"',`propreitir_name`='"+propri_name+"',`email`='"+ema+"',`phone`='"+ph+"',`place`='"+place+"',`post`='"+pst+"',`pin`='"+pin+"',`latitude`='"+ Latitude+"',`longitude`='"+Longitude+"' WHERE `man_lid`='"+str(session['lid'])+"'  "
    res = db.update(qry)
    return redirect('/profile_management_view')






@app.route('/profile_management_view')
def profile_management_view():
    db = Db()
    qry = "Select * from manufacturer where man_lid='"+str(session['lid'])+"'"
    res = db.selectOne(qry)
    if session['log'] == 'lin':
       return  render_template("Manufacters/ProfileManagment_View.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"





@app.route('/sign_up')
def sign_up():
    return render_template("Manufacters/SignUpPage.html")



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
        qry="INSERT INTO `manufacturer` (`name`,`propreitir_name`,`email`,`phone`,`place`,`post`,`pin`,`latitude`,`longitude`,`status`,passwd) VALUES('"+usrname+"','"+propri_name+"','"+ema+"','"+ph+"','"+place+"','"+pst+"','"+pin+"','"+Latitude+"','"+Longitude+"','pending','"+passwd+"')"
        res=db.insert(qry)
        return redirect('/')
    else:
        "<script>alert('Password dose not match');window.location='/sign_up'</script>"






@app.route('/staff_managment')
def staff_managment():
    db= Db()
    qry = "SELECT * FROM `staff` WHERE `man-id`= '"+str(session['lid'])+"' "
    res = db.select(qry)
    if session['log'] == 'lin':
       return render_template("Manufacters/StaffManagment-0.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"


@app.route('/staff_managment_post',methods=['post'])
def staff_managment_post():
    Search = request.form['textfield']
    db=Db()
    qry="SELECT * FROM `staff` WHERE `man-id`='"+str(session['lid'])+"' and sname like '"+Search+"'"
    res=db.select(qry)
    return render_template("Manufacters/StaffManagment-0.html",data=res)




@app.route('/staff_managment_add')
def staff_managment_add():
    if session['log'] == 'lin':
      return render_template("Manufacters/StaffManagment-AddNew.html")
    else:
        return "<script>alert('Log out');window.location='/'</script>"


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
    if session['log'] == 'lin':
       return render_template("Manufacters/StaffManagment-Edit.html",data=res)
    else:
        return "<script>alert('Log out');window.location='/'</script>"



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
    if session['log'] == 'lin':
       return "<script>alert('deleted');window.location='/staff_managment'</script>"
    else:
        return "<script>alert('Log out');window.location='/'</script>"




@app.route('/Change_passwords')
def Change_passwords():
    if session['log'] == 'lin':
       return render_template("Manufacters/ChangePasswords.html")
    else:
        return "<script>alert('Log out');window.location='/'</script>"




@app.route('/Change_passwords_post',methods=['post'])
def Change_passwords_post():
    current_pass = request.form['textfield']
    new_pass = request.form['textfield2']
    confirm_pass = request.form['textfield3']
    db = Db()
    qry="select * from login where password='"+current_pass+"' and lid='"+str(session['lid'])+"'"
    res=db.selectOne(qry)
    if res is not None:
        if new_pass==confirm_pass:
            qry1=" UPDATE `login` SET `password`='"+new_pass+"' WHERE `lid`='"+str(session['lid'])+"'"
            res=db.update(qry1)
    return '''<script>alert('Password changed Successfully');window.location='/profile_management_view'</script>'''


@app.route('/Home_Manufactors')
def Home_Manufactors():
    if session['log'] == 'lin':
       return render_template("Manufacters/HomePage0.html")
    else:
        return "<script>alert('Log out');window.location='/'</script>"


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#========================================Flutter========================================================================
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$





#=======================================================================================================================
#--------------------------------------------------------------Users----------------------------------------------------
#=======================================================================================================================


@app.route('/and_Login_post', methods=['POST'])
def and_Login_post():
    name=request.form['name']
    passwd=request.form['passwd']
    db = Db()
    qry = "select * from login where username='" + name + "' and password='" + passwd + "'"
    res = db.selectOne(qry)
    print(res)
    if res is not None:
        lid = res['lid']
        if res['type'] == 'user':
            return jsonify(status="ok", lid=lid,type="user")
        elif res['type'] == 'staff':
            return jsonify(status="ok", lid=lid,type="staff")
        else:
            return jsonify(status="no")
    else:
        return jsonify(status="no")


@app.route('/and_View_Profile_post', methods=['POST'])
def and_View_Profile_post():
    lid = request.form['lid']
    db = Db()
    qry = " SELECT * FROM `user`WHERE `user_lid`='"+lid+"' "
    res = db.selectOne(qry)
    if res is not None:
        return jsonify(status="ok", Name=res["naame"],Age=res["age"],Gender=res["gender"],Place=res["place"],Post=res["post"],Pin=res["pin"],Email=res["email"],Phone=res["phone"] )
    else:
        return jsonify(status="no")


@app.route('/and_signup_post', methods=['POST'])
def and_signup_post():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    passwd = request.form['passwd']
    # Cpasswd = request.form['Cpasswd']
    # if passwd==Cpasswd:
    db = Db()
    qry = " INSERT INTO `login`(`username`,`password`,`type`)VALUES('" + email + "','" + passwd + "','user')"
    res = db.insert(qry)
    qry1 = "INSERT INTO `user`(`naame`,`age`,`gender`,`place`,`post`,`pin`,`phone`,`email`,user_lid)VALUES('" + name + "','" + age + "','" + gender + "','" + place + "','" + post + "','" + pin + "','" + phone + "','" + email + "','"+str(res)+"')"
    res = db.insert(qry1)
    return jsonify(status="ok", data=res)





@app.route('/and_view_category', methods=['POST'])
def and_view_category():
    qry="SELECT * FROM `category`"
    db=Db()
    res=db.select(qry)
    print(res)
    return jsonify(status="ok",data=res)




@app.route('/and_view_product', methods=['POST'])
def and_view_product ():
    db=Db()
    qry="SELECT * FROM `product`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)




@app.route('/and_view_product_review', methods=['POST'])
def and_view_product_review():
    pid = request.form['pid']
    db=Db()
    qry="select * from `product_review`WHERE pid='"+pid+"' "
    res=db.select(qry)
    return jsonify(status="ok",data=res)




@app.route('/and_sent_product_review', methods=['POST'])
def and_sent_product_review():
    pid = request.form['pid']
    user = request.form['user']
    review = request.form['review']
    rating = request.form['rating']
    db=Db()
    qry=" INSERT INTO `product_review`(`pid`,`user_lid`,`review`,`rating`,`date`)VALUES('"+pid+"','"+user+"','"+review+"','"+rating+"',curdate()) "
    res=db.insert(qry)
    return jsonify(status="ok",data=res)




@app.route('/and_sent_delivery_rating', methods=['POST'])
def and_view_delivery_rating():
    assignID = request.form['assignID']
    rating = request.form['rating']
    review = request.form['review']
    date = request.form['date']
    db=Db()
    qry = " INSERT INTO `delivery_rating`(`assign_id`,`rating`,`review`,`date`)VALUES('"+assignID+"','"+rating+"','"+review+"','"+date+"') "
    res = db.insert(qry)
    return jsonify(status="ok",data=res)



@app.route('/and_sent_complaints', methods=['POST'])
def and_sent_complaints():
    pid=request.form["pid"]
    user = request.form['user']
    complaint = request.form['complaint']
    db=Db()
    qry = " INSERT INTO `compalint`(`user_lid`,`complaint`,`status`,`date`,replay,pid)VALUES('"+user+"','"+complaint+"','pending',curdate(),'pending','"+pid+"') "
    res = db.insert(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_view_complaint', methods=['POST'])
def and_view_complaint():
    pid = request.form['pid']
    df
    return jsonify(status="ok", data=res)


@app.route('/and_view_reply', methods=['POST'])
def and_view_reply():
    user = request.form['user']
    db=Db()
    qry = " SELECT * FROM `compalint` WHERE `user_lid`='"+user+"' "
    res = db.select(qry)
    print(res)
    return jsonify(status="ok",data=res)



@app.route('/and_add_to_cart', methods=['POST'])
def and_add_to_cart():
    product = request.form['product']
    user = request.form['user']
    qty = request.form['qty']
    db=Db()
    qry = " INSERT INTO `cart`(`pid`,`user_id`,`qty`) VALUES('"+product+"','"+user+"','"+qty+"') "
    res = db.insert(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_view_cart', methods=['POST'])
def and_view_cart():
    product = request.form['product']
    db=Db()
    qry = " SELECT * FROM cart JOIN `product` ON `product`.`pid`=`cart`.`pid` WHERE `cart`.pid='"+product+"' "
    res = db.select(qry)
    return jsonify(status="ok",data=res)



@app.route('/and_remove_Cart', methods=['POST'])
def and_remove_Cart():
    product = request.form['product']
    db=Db()
    qry = " delete from cart where pid='"+product+"' "
    res = db.delete(qry)
    return jsonify(status="ok",data=res)


@app.route('/and_EditProfile_post', methods=['POST'])
def and_EditProfile_post():
    lid = request.form['lid']
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']

    db = Db()
    qry = " UPDATE `user` SET `naame`='"+name+"',`age`='"+age+"',`gender`='"+gender+"',`place`='"+place+"',`post`='"+post+"',`pin`='"+pin+"',`phone`='"+phone+"'   WHERE `user_lid`= '"+lid+"' "
    res = db.update(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_View_SingleProduct_post', methods=['POST'])
def and_View_SingleProduct_post():
    pid = request.form['pid']
    db =Db()
    qry = " SELECT * FROM `product` WHERE `pid`='"+pid+"' "
    res = db.selectOne(qry)
    print(res)
    if res is not None:
        return jsonify(status="ok",Name=res["product_name"],Price=res["price"],description=res["description"],photo=res["photo"] )
    else:
        return jsonify(status="no")


#========================================staff======================================================

@app.route('/View_Profile', methods=['POST'])
def View_Profile():
    lid = request.form['lid']
    db = Db()
    qry = " SELECT * FROM `staff`WHERE `staff-lid`="'+lid+'""
    res = db.select(qry)
    return jsonify(status="ok", data=res)


@app.route('/View_assigned_order', methods=['POST'])
def View_assigned_order():
    lid = request.form['lid']
    db = Db()
    qry = " SELECT * FROM  `deliverry_assign` JOIN `order_main` ON `order_main`.`order_id` = `deliverry_assign`.`order_id` JOIN `order_sub` ON `order_sub`.`order_id` = `order_main`.`order_id` JOIN `product` ON `product`.`pid` = `order_sub`.`pid` JOIN `user` ON `user`.`user_lid` = `order_main`.`user-lid` WHERE `deliverry_assign`.`staff_id` = '"+lid+"' and `deliverry_assign`.`status`='p' "
    res = db.select(qry)
    return jsonify(status="ok", data=res)



@app.route('/View_rating', methods=['POST'])
def View_rating():
    lid = request.form['lid']
    db = Db()
    qry = " SELECT * FROM `delivery_rating` JOIN `deliverry_assign` ON  `deliverry_assign`.`assign_id`= `delivery_rating`.`assign_id` JOIN order_main ON order_main.`order_id`=  deliverry_assign.`order_id` JOIN `user`ON `user`.`user_lid`=`order_main`.`user-lid` WHERE `deliverry_assign`.`staff_id`='"+lid+"' "
    res = db.select(qry)
    return jsonify(status="ok", data=res)



@app.route('/View_previous_order', methods=['POST'])
def View_previous_order():
    lid = request.form['lid']
    db = Db()
    qry = " SELECT * FROM  `deliverry_assign` JOIN `order_main` ON `order_main`.`order_id` = `deliverry_assign`.`order_id`   JOIN `user` ON `user`.`user_lid` = `order_main`.`user-lid` WHERE `deliverry_assign`.`staff_id` = '"+lid+"' "
    res = db.select(qry)
    return jsonify(status="ok", data=res)



app.run(debug=True,host='0.0.0.0')