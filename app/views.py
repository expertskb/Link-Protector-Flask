from flask import render_template, request, session, redirect, flash, send_from_directory, abort
from . import db
from .models import Link
import random
import string
import re
import os

def home():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        body = request.form['body']
        
        if not body:
            flash('Links not found', 'warning')
            return redirect('/')
        
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        
        link = Link(fid=random_string, data=body, name=name, password=password, views=0)
        
        db.session.add(link)
        db.session.commit()
        
        link_url = f"https://{request.host}/view/{random_string}"
        
        flash(link_url, 'success')
        
    return render_template('index.html')

def view(fid):
    data = Link.query.filter_by(fid=fid).first()
    
    if not data:
        return redirect('/')
    
    data.views += 1
    db.session.commit()
    
    regExUrl = r'(ftp|https?):\/\/(\w+:?\w*@)?([^\s]+)(:[0-9]+)?(\/[^\s]*)?'
    
    content = data.data
    
    links = re.sub(regExUrl, r'<a href="\g<0>" rel="external" target="_blank">\g<0></a><p>', content)
    
    return render_template('view.html', 
                           data=data,
                           links=links)
