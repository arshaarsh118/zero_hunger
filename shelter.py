from flask import*
from database import*

shelter=Blueprint('shelter',__name__)

@shelter.route('/shelterhome')
def shelterhome():
    return render_template('shelterhome.html')

@shelter.route('/shelter_view_profile',methods=['POST','GET'])
def shelter_view_profile():
    data={}
    a="select * from shelter where shelter_id='%s'"%(session['shelter'])
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'update':
            p="select * from shelter where shelter_id='%s'"%(id)
            q=select(p)
            if q:
                data['up']=q
                if 'update' in request.form:
                   
                    name=request.form['name']
                    phone=request.form['phone']
                    email=request.form['email']
                    address=request.form['address']
                    capacity=request.form['capacity']
                    place=request.form['place']
                    pincode=request.form['pincode']
                    district=request.form['dis']
                    r="update shelter set shelter_name='%s',shelter_phone='%s',shelter_email='%s',shelter_address='%s',shelter_capacity='%s',shelter_place='%s',shelter_pincode='%s',shelter_district='%s' where shelter_id='%s'"%(name,phone,email,address,capacity,place,pincode,district,id)
                    s=update(r)
                    if s:
                        return '''<script>alert("Edit Sucessfully");window.location="/shelterhome"</script>'''
                    
        if action == 'delete':
            t="delete from shelter where shelter_id='%s'"%(id)
            delete(t)
            return '''<script>alert("Delete Sucessfully");window.location="/shelterhome"</script>''' 
    return render_template('shelter_view_profile.html',data=data)

from datetime import datetime

@shelter.route('/shelter_view_surplus')
def shelter_view_surplus():
    data={}
    a="select * from surplus_food inner join item using(item_id)"
    b=select(a)
    if b:
        data['view']=b
    

    current_date = datetime.now().strftime('%Y-%m-%d')
    for item in data['view']:
    # Convert expiration_date to string if it's not already
        expiry_date = str(item['expiration_date'])
    
    # Compare dates as strings (assuming format is YYYY-MM-DD)
    item['is_expired'] = expiry_date < current_date
        
    return render_template('shelter_view_surplus.html',data=data,current_date=current_date)

@shelter.route('/shelter_view_order')
def shelter_view_order():
    data={}
    a="SELECT * FROM `surplus_request` INNER JOIN `surplus_food` USING(surplus_id) INNER JOIN `item` USING(item_id) where shelter_id='%s'"%(session['shelter'])
    b=select(a)
   

    if b:
        data['view']=b
    return render_template('shelter_view_order.html',data=data)

@shelter.route('/shelter_change_password',methods=['POST','GET'])
def shelter_change_password():
    if 'update' in request.form:
        password=request.form['password']
        password1=request.form['password1']
        if password==password1:

                   
            r="update login set password='%s' where login_id='%s'"%(password1,session['log'])
            s=update(r)
            if s:
                return '''<script>alert("Change Sucessfully");window.location="/shelter_change_password"</script>'''
            
        else:
            return '''<script>alert("Confirm Your Entered Password");window.location="/shelter_change_password"</script>'''
                    
    return render_template('shelter_change_password.html')

@shelter.route('/shelter_send_req',methods=['POST','GET'])
def shelter_send_req():
    id=request.args['id']
    surplus_qty=request.args['surplus_qty']
    if 'submit' in request.form:
        quantity=request.form['quantity']
        if int(quantity)>int(surplus_qty):
            return'''<script>alert("out off stock");window.location="/shelter_view_surplus"</script>'''
        else:

            a="insert into surplus_request values(null,'%s','%s','%s',curdate(),'pending')"%(session['shelter'],id,quantity)
            b=insert(a)
            if b:
                return '''<script>alert("Order Request Send Sucessfully");window.location="/shelter_view_surplus"</script>'''
                        
    return render_template('shelter_send_req.html')



