from flask import*
from database import*

distributor=Blueprint('distributor',__name__)

@distributor.route('/distributorhome')
def distributorhome():
    return render_template('distributorhome.html')

@distributor.route('/distributor_view_profile',methods=['post','get'])
def distributor_view_profile():
    data={}
    a="select * from distributor where distributor_id='%s'"%(session['distributor'])
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'update':
            p="select * from distributor where distributor_id='%s'"%(id)
            q=select(p)
            if q:
                data['up']=q
                if 'update' in request.form:
                    name=request.form['name']
                    phone=request.form['phone']
                    email=request.form['email']
                    place=request.form['place']
                    pincode=request.form['pincode']
                    district=request.form['district']
                    r="update distributor set distributor_name='%s',distributor_phone='%s',distributor_email='%s',distributor_place='%s',distributor_pincode='%s',distributor_district='%s' where distributor_id='%s'"%(name,phone,email,place,pincode,district,id)
                    s=update(r)
                    if s:
                        return '''<script>alert("Edit Sucessfully");window.location="/distributor_view_profile"</script>'''
                    
       
    return render_template('distributor_view_profile.html',data=data)

@distributor.route('/distributor_view_farmer')
def distributor_view_farmer():
    data={}
    a="select * from farmer"
    b=select(a)
    if b:
        data['view']=b
    return render_template('distributor_view_farmer.html',data=data)

@distributor.route('/distributor_search_item')
def distributor_search_item():
    id=request.args['id']
    data={}
    a="select * from farmer_item inner join item using(item_id) where farmer_id='%s'"%(id)
    b=select(a)
    if b:
        data['view']=b
    return render_template('distributor_search_item.html',data=data)

@distributor.route('/distributor_add_to_cart',methods=['post','get'])
def distributor_add_to_cart():
    id=request.args['id']
    amount=request.args['amount']
    stock=request.args['stock']
    if 'submit' in request.form:
        quantity=request.form['quantity']
        if int(quantity)>int(stock):
            return'''<script>alert("out off stock");window.location="/distributor_view_farmer"</script>'''
        else:
            
            total=int(amount)*int(quantity)
       
            x="select * from order_master where om_status='pending' and distributor_id='%s'"%(session['distributor'])
            y=select(x)

    

            if y:
                omid=y[0]['om_id']
                om_total=y[0]['om_total']
                cart_total=int(total)+int(om_total)
                z="update order_master set om_total='%s' where om_id='%s'"%(cart_total,omid)
                update(z)
                a="insert into order_details values(null,'%s','%s','%s','%s',curdate())"%(omid,id,quantity,amount)
                insert(a)
                return redirect(url_for('distributor.distributor_view_farmer'))

            else:
                p="insert into order_master values(null,'%s','%s',curdate(),'pending')"%(session['distributor'],total)
                b=insert(p)

                c="insert into order_details values(null,'%s','%s','%s','%s',curdate())"%(b,id,quantity,amount)
                insert(c)
                return redirect(url_for('distributor.distributor_view_farmer'))
            
        
    return render_template('distributor_add_to_cart.html')

@distributor.route('/distributor_view_cart',methods=['post','get'])
def distributor_view_cart():
   

    data={}
    a="select * from order_master inner join order_details using(om_id) inner join item using(item_id) inner join farmer_item using(item_id) where distributor_id='%s' and om_status='pending'"%(session['distributor'])
    b=select(a)
    if b:
        data['view']=b
        print(b,"___________________________________")

        if 'action' in request.args:
            action=request.args['action']
            id=request.args['id'] 
            amt=request.args['amt']
            odamt=request.args['odamt'] 
            if action =='delete':
                d="delete from order_details where od_id='%s'"%(id)
                delete(d)
                if b:
                    omid=b[0]['om_id']
                    cur_amt=int(amt)-int(odamt)
                    e="update order_master set om_total='%s' where om_id='%s'"%(cur_amt,omid)
                    update(e)
                return '''<script>alert("remove sucessfully");window.location="/distributor_view_cart"</script>'''      
    else:
        return '''<script>alert("no cart");window.location="/distributor_view_farmer"</script>'''
    return render_template('distributor_view_cart.html',data=data)

@distributor.route('/distributor_payment',methods=['post','get'])
def distributor_payment():
    id=request.form['om_id']
    fid=request.form['farmer_id']

    amt=request.form['tot_amt']
    stock=request.form['farmer_item_st']
    quan=request.form['od_quantity']

    stk=int(stock)-int(quan)
    print(stk)

    
    if 'submit' in request.form:
        # Payment=request.form['payment']

        z="insert into order_payment values(null,'%s','%s',curdate(),'paid')"%(id,amt)   
        a=insert(z)
        if a:  
            stat="update order_master set om_status='paid' where om_id='%s'"%(id)
            update(stat)
        
            b="select * from order_details inner join order_master using (om_id) inner join item using(item_id) where om_id='%s'"%(id)
            c=select(b)

            x="update farmer_item set farmer_item_stock='%s' where farmer_item_id='%s'"%(stk,fid)
            w=update(x)
            if w:
                return '''<script>alert("Payment Completed Successfully");window.location="/distributor_search"</script>'''

              
    return render_template('distributor_payment.html',amt=amt)

@distributor.route('/distributor_add_surplus',methods=['post','get'])
def distributor_add_surplus():
    data={}
    b="select * from item"
    c=select(b)
    if c:
        data['view']=c

    if 'submit' in request.form:
        item=request.form['item']
        quantity=request.form['quantity']
        type=request.form['type']
        date=request.form['date']
        requirement=request.form['requirement']
        name=request.form['name']
        phone=request.form['phone']
        location=request.form['location']
        a="insert into surplus_food values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(item,quantity,type,date,requirement,name,phone,location)
        insert(a)

    data1={}
    a="select * from surplus_food inner join item using(item_id)"
    b=select(a)
    if b:
        data1['view']=b
    return render_template('distributor_add_surplus.html',data=data,data1=data1)

@distributor.route('/distributor_view_req')
def distributor_view_req():
    data={}
    a="select * from surplus_request inner join shelter using(shelter_id) inner join surplus_food using(surplus_id) inner join item using(item_id)"
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
            if action == 'accept':
                q="update surplus_request set surplus_req_status='accept' where request_id='%s'"%(id)
                r=update(q)
                if r:
                    s="SELECT * FROM `surplus_food` INNER JOIN `surplus_request` USING(surplus_id) where request_id='%s'"%(id)
                    t=select(s)
                    if t:
                        for item in t:
                            surplus_stk = item['quantity_details']
                            surplus_qty = item['surplus_qty_details']
                            sur_id = item['surplus_id']
                            cur_stk = int(surplus_stk) - int(surplus_qty)
                            u = "update surplus_food set quantity_details='%s' where surplus_id='%s'" % (cur_stk, sur_id)
                            v = update(u)
                            if u:
                                return '''<script>alert("Approved");window.location="/distributor_view_req"</script>'''

    
            if action == 'reject':
                q1="update surplus_request set surplus_req_status='rejected' where request_id='%s'"%(id)
                update(q1)
                return '''<script>alert("Rejected");window.location="/distributor_view_req"</script>'''
            
    data1={}
    c="select * from surplus_request inner join shelter using(shelter_id) inner join surplus_food using(surplus_id) inner join item using(item_id) where surplus_req_status='accept'" 
    d=select(c)
    if d:
        data1['view']=d 

    data2={}
    c="select * from surplus_request inner join shelter using(shelter_id) inner join surplus_food using(surplus_id) inner join item using(item_id) where surplus_req_status='rejected'" 
    d=select(c)
    if d:
        data2['view']=d     
    
    
    return render_template('distributor_view_req.html',data=data,data1=data1,data2=data2)


@distributor.route('/distributor_search', methods=['GET', 'POST'])
def distributor_search():
    data = {}
    if 'submit' in request.form:
        sr = request.form['search']
        z = f"select * from farmer_item inner join item using(item_id) WHERE item_name LIKE '%{sr}%'"
        data['search'] = select(z)
    else:
        a = "select * from farmer_item inner join item using(item_id)"
        b = select(a)
        if b:
            data['view'] = b

    return render_template('distributor_search.html', data=data)

