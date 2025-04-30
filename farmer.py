from flask import*
from database import*

farmer=Blueprint('farmer',__name__)

@farmer.route('/farmerhome')
def farmerhome():
    return render_template('farmerhome.html')

@farmer.route('/farmer_view_profile',methods=['POST','GET'])
def farmer_view_profile():
    data={}
    a="select * from farmer where farmer_id='%s'"%(session['farmer'])
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'update':
            p="select * from farmer where farmer_id='%s'"%(id)
            q=select(p)
            if q:
                data['up']=q
                if 'update' in request.form:
                    fname=request.form['fname']
                    place=request.form['place']
                    pin=request.form['pin']
                    dob=request.form['dob']
                    phone=request.form['phone']
                    email=request.form['email']
                    r="update farmer set farmer_name='%s',farmer_place='%s',farmer_pincode='%s',farmer_dob='%s',farmer_dob='%s',farmer_email='%s' where farmer_id='%s'"%(fname,place,pin,dob,phone,email,id)
                    s=update(r)
                    if s:
                        return '''<script>alert("Edit Sucessfully");window.location="/farmerhome"</script>'''
    return render_template('farmer_view_profile.html',data=data)

@farmer.route('/farmer_add_item',methods=['POST','GET'])
def farmer_add_item():
    data={}
    a="select * from item"
    b=select(a)
    if b:
        data['view']=b

    if 'submit' in request.form:
        item=request.form['item']
        stock=request.form['stock']
        c="insert into farmer_item values(null,'%s','%s','%s')"%(session['farmer'],item,stock)
        insert(c)
    data1={}
    d="select * from farmer_item inner join farmer using(farmer_id) inner join item using(item_id) where farmer_id='%s'"%(session['farmer'])
    e=select(d)
    if e:
        data1['view']=e

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    
    else:
        action=None

    if action == 'update':
            p="select * from farmer_item where farmer_item_id='%s'"%(id)
            q=select(p)
            if q:
                data1['up']=q
    if 'up' in request.form:
                    stock=request.form['stock']
                    r="update farmer_item set farmer_item_stock='%s' where farmer_item_id='%s'"%(stock,id)
                    s=update(r)
                    if s:
                        return '''<script>alert("Update Sucessfully");window.location="/farmer_add_item"</script>'''
                    
    if action == 'delete':
            t="delete from farmer_item where farmer_item_id='%s'"%(id)
            delete(t)
            return '''<script>alert("Delete Sucessfully");window.location="/farmer_add_item"</script>''' 
    return render_template('farmer_add_item.html',data=data,data1=data1)

@farmer.route('/farmersend_complaint',methods=['get','post'])
def farmersend_complaint():
    if 'submit' in request.form:
        complaint=request.form['complaint']
        a="insert into complaint values(null,'%s','%s','No Replay',curdate())"%(session['log'],complaint)
        insert(a)

    data={}
    b="select * from complaint where login_id='%s'"%(session['log'])
    c=select(b)
    if c:
        data['view']=c
    return render_template('farmersend_complaint.html',data=data)


@farmer.route('/farmer_view_payment',methods=['POST','GET'])
def farmer_view_payment():

    data={}
    a="SELECT * FROM order_payment INNER JOIN order_master USING(om_id) INNER JOIN order_details USING(om_id) INNER JOIN item USING(item_id) INNER JOIN farmer_item USING(item_id) INNER JOIN farmer USING(farmer_id) where farmer_id='%s'"%(session['farmer'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('farmer_view_payment.html',data=data)

@farmer.route('/farmer_view_order')
def farmer_view_order():
    data={}
    x="select * from order_master inner join order_details using(om_id) inner join item using(item_id) INNER JOIN farmer_item USING(item_id) where om_status='paid' and farmer_id='%s'"%session['farmer']
    y=select(x)
    if y:
        data['view']=y
    # else:
    #     return '''<script>alert("you have no orders");window.location="/user_view_spare_parts"</script>'''
    return render_template('farmer_view_order.html',data=data)

