from flask import*
from database import*
import uuid


admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/admin_manage_item',methods=['post','get'])
def admin_manage_item():
    if 'submit' in request.form:
        item=request.form['item']
        price=request.form['price']
        a="insert into item values(null,'%s','%s')"%(item,price)
        z=insert(a)
        if z:
            return '''<script>alert("Add Sucessfully");window.location="/admin_manage_item"</script>'''


    data={}
    b="select * from item"
    c=select(b)
    if c:
        data['view']=c

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'update':
            p="select * from item where item_id='%s'"%(id)
            q=select(p)
            if q:
                data['up']=q
                if 'update' in request.form:
                    item=request.form['item']
                    price=request.form['price']
                    r="update item set item_name='%s',item_price='%s' where item_id='%s'"%(item,price,id)
                    s=update(r)
                    if s:
                        return '''<script>alert("Update Sucessfully");window.location="/admin_manage_item"</script>'''
                    
        if action == 'delete':
            t="delete from item where item_id='%s'"%(id)
            delete(t)
            return '''<script>alert("Delete Sucessfully");window.location="/admin_manage_item"</script>''' 
    return render_template('admin_manage_item.html',data=data)

@admin.route('/admin_view_farmer')
def admin_view_farmer():
    data={}
    a="select * from farmer inner join login using(login_id)"
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
            if action == 'accept':
                q="update login set usertype='farmer' where login_id='%s'"%(id)
                r=update(q)
                if r:
                
                    return '''<script>alert("Approved");window.location="/admin_view_farmer"</script>'''
    
            if action == 'reject':
                q1="update login set usertype='rejected' where login_id='%s'"%(id)
                q2=update(q1)
                if q2:

                    return '''<script>alert("Rejected");window.location="/admin_view_farmer"</script>'''
            
    return render_template('admin_view_farmer.html',data=data)

@admin.route('/admin_view_distribution')
def admin_view_distribution():
    data={}
    a="select * from distributor inner join login using(login_id)"
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
            if action == 'accept':
                q="update login set usertype='distributor' where login_id='%s'"%(id)
                r=update(q)
                if r:
                    data['acc']=r
                    if 'accept' in request.form:
                        s="select * from distributor inner join login using(login_id) where usertype='distributor'"
                        select(s)
                return '''<script>alert("Approved");window.location="/admin_view_distribution"</script>'''
    
            if action == 'reject':
                q1="update login set usertype='rejected' where login_id='%s'"%(id)
                update(q1)
                return '''<script>alert("Rejected");window.location="/admin_view_distribution"</script>'''
            
    data1={}
    c="select * from distributor inner join login using(login_id) where usertype='distributor'" 
    d=select(c)
    if d:
        data1['view']=d 

    data2={}
    c="select * from distributor inner join login using(login_id) where usertype='rejected'" 
    d=select(c)
    if d:
        data2['view']=d     
    
    return render_template('admin_view_distribution.html',data=data,data1=data1,data2=data2)

@admin.route('/admin_view_shelter')
def admin_view_shelter():
    data={}
    a="select * from shelter inner join shelter_type using(type_id) inner join login using(login_id)"
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
            if action == 'accept':
                q="update login set usertype='shelter' where login_id='%s'"%(id)
                r=update(q)
                if r:
                    return '''<script>alert("Approved");window.location="/admin_view_shelter"</script>'''
    
            if action == 'reject':
                q1="update login set usertype='rejected' where login_id='%s'"%(id)
                r1=update(q1)
                if r1:
                    return '''<script>alert("Rejected");window.location="/admin_view_shelter"</script>'''
    return render_template('admin_view_shelter.html',data=data)

@admin.route('/admin_view_complaint')
def admin_view_complaint():
    data={}
    a="select * from complaint inner join login using(login_id)"
    b=select(a)
    if b:
        data['view']=b
    
    return render_template('admin_view_complaint.html',data=data)

@admin.route('/admin_send_reply',methods=['get','post'])
def admin_send_reply():
    id=request.args['id']
    if 'send' in request.form:
        reply=request.form['reply']
        a="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
        update(a)
        return '''<script>alert("replay sending completed");window.location="/admin_view_complaint"</script>''' 
    return render_template('admin_send_reply.html')

@admin.route('/admin_view_surplus')
def admin_view_surplus():
    a="select * from surplus_request inner join  shelter using(shelter_id) inner join surplus_food using(surplus_id) inner join item using(item_id)"
    data={}
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_surplus.html',data=data)

@admin.route('/admin_view_surplus_req')
def admin_view_surplus_req():
    a="select * from surplus_request inner join surplus_food using(surplus_id) inner join item using(item_id) inner join shelter using(shelter_id)"
    data={}
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_surplus_req.html',data=data)

@admin.route('/admin_change_password',methods=['POST','GET'])
def admin_change_password():
    
    if 'update' in request.form:
        password=request.form['password']
        password1=request.form['password1']
        if password==password1:

                   
            r="update login set password='%s' where login_id='%s'"%(password1,session['log'])
            s=update(r)
            if s:
                return '''<script>alert("Change Sucessfully");window.location="/admin_change_password"</script>'''
            
        else:
            return '''<script>alert("Confirm Your Entered Password");window.location="/admin_change_password"</script>'''

                    
    return render_template('admin_change_password.html')

@admin.route('/admin_manage_video',methods=['post','get'])
def admin_manage_video():
    if 'submit' in request.form:
        title=request.form['title']
        description=request.form['dis']
        file=request.files['file']
        filetype=request.form['filetype']
        path='static/'+str(uuid.uuid4())+file.filename
        file.save(path)

        a="insert into tutorial values(null,'%s','%s','%s','%s')"%(title,description,path,filetype)
        x=insert(a)
        if x:
            return '''<script>alert("Video Added Sucessfully");window.location="/admin_manage_video"</script>'''

    data={}
    b="select * from tutorial"
    c=select(b)
    if c:
        data['view']=c

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'update':
            p="select * from tutorial where tutorial_id='%s'"%(id)
            q=select(p)
            if q:
                data['up']=q
                if 'update' in request.form:
                    title=request.form['title']
                    description=request.form['dis']
                    file=request.files['file']
                    filetype=request.form['filetype']
                    path='static/'+str(uuid.uuid4())+file.filename
                    file.save(path)

                    r="update tutorial set title='%s',description='%s',file_path='%s',file_type='%s' where tutorial_id='%s'"%(title,description,path,filetype,id)
                    s=update(r)
                    if s:
                        return '''<script>alert("Update Sucessfully");window.location="/admin_manage_video"</script>'''
                    
        if action == 'delete':
            t="delete from tutorial where tutorial_id='%s'"%(id)
            u=delete(t)
            if u:

                return '''<script>alert("Delete Sucessfully");window.location="/admin_manage_video"</script>''' 
    return render_template('admin_manage_video.html',data=data)

@admin.route('/admin_manage_type',methods=['post','get'])
def admin_manage_type():
    if 'submit' in request.form:
        type=request.form['type']
        a="insert into shelter_type values(null,'%s')"%(type)
        b=insert(a)
        if b:
            return '''<script>alert("Added Successfully");window.location="/admin_manage_type"</script>'''

    data={}
    c="select * from shelter_type" 
    d=select(c)
    if d:
        data['view']=d

    if 'action' in request.args:
        act=request.args['action']
        id=request.args['id']
        if act == 'update':
            e="select * from shelter_type where type_id='%s'"%(id)
            f=select(e)
            if f:
                data['up']=f
                if 'update' in request.form:
                    type=request.form['type']
                    g="update shelter_type set shelter_type='%s' where type_id='%s'"%(type,id)
                    h=update(g)
                    if h:
                        return '''<script>alert("Updated Successfully");window.location="/admin_manage_type"</script>'''
                    
        if act == 'delete':
            t="delete from shelter_type where type_id='%s'"%(id)
            u=delete(t)
            if u:

                return '''<script>alert("Delete Sucessfully");window.location="/admin_manage_type"</script>''' 

    return render_template('admin_manage_type.html',data=data)




@admin.route('/admin_view_count')
def admin_view_count():
    data={}
    a="SELECT * FROM surplus_request INNER JOIN surplus_food USING(surplus_id)"
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_count.html',data=data)






