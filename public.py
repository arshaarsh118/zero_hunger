from flask import*
from database import*

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['POST','GET'])
def login():
    if 'submit' in request.form:
        uname=request.form['uname']
        password=request.form['password']

        a="select * from login where username='%s' and password='%s'"%(uname,password)
        b=select(a)

        if b:
            session['log']=b[0]['login_id']
            
            if b[0]['usertype']=='farmer':
                c="select * from farmer where login_id='%s'"%(session['log'])
                d=select(c)
                if d:
                    session['farmer']=d[0]['farmer_id']
                    return redirect(url_for('farmer.farmerhome'))
                
            if b[0]['usertype']=='shelter':
                x="select * from shelter where login_id='%s'"%(session['log'])
                y=select(x)
                if y:
                    session['shelter']=y[0]['shelter_id']
                    return redirect(url_for('shelter.shelterhome'))
                
            if b[0]['usertype']=='distributor':
                aa="select * from distributor where login_id='%s'"%(session['log'])
                bb=select(aa)
                if bb:
                    session['distributor']=bb[0]['distributor_id']
                    return redirect(url_for('distributor.distributorhome'))
                
            if b[0]['usertype']=='admin':
                return redirect(url_for('admin.adminhome'))

    return render_template('login.html')

@public.route('/farmer',methods=['POST','GET'])
def user():
    if 'submit' in request.form:
        fname=request.form['fname']
        place=request.form['place']
        pin=request.form['pin']
        dob=request.form['dob']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        password=request.form['password']

        a="insert into login values(null,'%s','%s','pending')"%(uname,password)
        b=insert(a)

        c="insert into farmer values(null,'%s','%s','%s','%s','%s','%s','%s')"%(b,fname,place,pin,dob,phone,email)
        d=insert(c)
        if d:
            return '''<script>alert("Farmer Registered Successfully");window.location="/login"</script>'''

    return render_template('farmer.html')

@public.route('/shelter',methods=['POST','GET'])
def shelter():

    data={}
    d="select * from shelter_type"
    e=select(d)
    if e:
        data['type']=e

    if 'submit' in request.form:
        type=request.form['type']
        name=request.form['name']
        phone=request.form['phone']
        email=request.form['email']
        address=request.form['address']
        capacity=request.form['capacity']
        place=request.form['place']
        pincode=request.form['pincode']
        district=request.form['dis']
        uname=request.form['uname']
        password=request.form['password']

        a="insert into login values(null,'%s','%s','pending')"%(uname,password)
        b=insert(a)

        c="insert into shelter values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(b,type,name,phone,email,address,capacity,place,pincode,district)
        d=insert(c)
        if d:
            return '''<script>alert("Shelter Registered Successfully");window.location="/login"</script>'''

    return render_template('shelter.html',data=data)

@public.route('/public_view_video')
def public_view_video():
    data={}
    a="select * from tutorial"
    b=select(a)
    if b:
        data['view']=b
    return render_template('public_view_video.html',data=data)

@public.route('/distributor',methods=['POST','GET'])
def distributor():
    if 'submit' in request.form:
        name=request.form['name']
        phone=request.form['phone']
        email=request.form['email']
        place=request.form['place']
        pincode=request.form['pincode']
        district=request.form['district']
        username=request.form['uname']
        password=request.form['password']
        a="insert into login values(null,'%s','%s','pending')"%(username,password)
        b=insert(a)
        c="insert into distributor values(null,'%s','%s','%s','%s','%s','%s','%s')"%(b,name,phone,email,place,pincode,district)
        d=insert(c)
        if d:
            return '''<script>alert("Distributor Registered Successfully");window.location="/login"</script>'''
    return render_template('distributor.html')

@public.route('/change_password',methods=['POST','GET'])
def change_password():
    data={}
    a="select * from login"
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'update':
            p="select * from login where login_id='%s'"%(id)
            q=select(p)
            if q:
                data['up']=q
                if 'update' in request.form:
                    password=request.form['password']
                   
                    r="update login set password='%s' where login_id='%s'"%(password,id)
                    s=update(r)
                    if s:
                        return '''<script>alert("Change Sucessfully");window.location="/admin_change_password"</script>'''
                    
    return render_template('change_password.html',data=data)
