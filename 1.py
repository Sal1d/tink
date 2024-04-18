from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import fitz

def add_font(p,fnt,fntf):
        p.insert_text(fitz.Point(x=0,y=0),"1",fontname=fnt,fontfile='d\\fonts\\dsText\\600.ttf',render_mode=3)

def edit(p,st,replace,fnt,size,align,color=(0,0,0),hit=0,y_diff=0):
    hit=p.search_for(st)[hit]
    if align==fitz.TEXT_ALIGN_RIGHT:
        x1=hit.x1
        y0=hit.y0-y_diff
        x0=0
        y1=hit.y1+10
    elif align==fitz.TEXT_ALIGN_LEFT:
        x1=hit.x1+10
        y0=hit.y0-y_diff
        x0=hit.x0
        y1=hit.y1+10
    else:
        x1=hit.x1
        y0=hit.y0
        x0=hit.x0
        y1=hit.y1
    p.add_redact_annot(hit)
    p.apply_redactions(images=0,graphics=0)
    p.insert_textbox(rect=fitz.Rect(x0=x0,y0=y0,x1=x1,y1=y1),buffer=replace,fontsize=size,fontname=fnt,color=color,align=align)

def tink_sbp_out(vr,cost,send,phone,recv,recvbank,id):
    doc=fitz.open('d/tink-sbp-out.pdf')
    p=doc[0]
    add_font(p,'FntT400','d\\fonts\\dsText\\400.ttf')
    add_font(p,'FntH400','d\\fonts\\dsHeading\\400.ttf')
    add_font(p,'EEX','d\\fonts\\EEX.ttf')
    edit(p,'1-13-540-458-735',id,'FntH400',9,fitz.TEXT_ALIGN_LEFT)
    edit(p,'Сбербанк',recvbank,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'Милана Б.',recv,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'+7 (911) 199-10-58',phone,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'Владислав Скрябин',send,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'500',cost,'EEX',15,fitz.TEXT_ALIGN_RIGHT,(0.2,0.2,0.2),0,-1)
    edit(p,'25.02.2024 19:29:24',vr,'FntT400',8,fitz.TEXT_ALIGN_LEFT,(0.5647058823529412,0.5647058823529412,0.5647058823529412))
    edit(p,'500',cost,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    
    return doc

def tink_tink_out(vr,cost,send,phone,recv,id):
    doc=fitz.open('d/tink-tink-out.pdf')
    p=doc[0]
    add_font(p,'FntT400','d\\fonts\\dsText\\400.ttf')
    add_font(p,'FntH400','d\\fonts\\dsHeading\\400.ttf')
    add_font(p,'EEX','d\\fonts\\EEX.ttf')
    edit(p,'1-13-717-033-312',id,'FntH400',9,fitz.TEXT_ALIGN_LEFT)
    edit(p,'Михаил С.',recv,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'+7 (911) 088-72-91',phone,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'Владислав Скрябин',send,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'100',cost,'EEX',15,fitz.TEXT_ALIGN_RIGHT,(0.2,0.2,0.2),0,-1)
    edit(p,'05.03.2024 17:32:47',vr,'FntT400',8,fitz.TEXT_ALIGN_LEFT,(0.5647058823529412,0.5647058823529412,0.5647058823529412))
    edit(p,'100',cost,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    
    return doc

def sbp_tink_in(vr,cost,phone,bankcode,id):
    doc=fitz.open('d/sbp-tink-in.pdf')
    p=doc[0]
    add_font(p,'FntT400','d\\fonts\\dsText\\400.ttf')
    add_font(p,'FntH400','d\\fonts\\dsHeading\\400.ttf')
    edit(p,'2-11-993-662-247',id,'FntH400',9,fitz.TEXT_ALIGN_LEFT)
    edit(p,'011993662247',bankcode,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'+7 (981) 032-89-83',phone,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'25.02.2024 19:22:33',vr,'FntT400',8,fitz.TEXT_ALIGN_LEFT,(0.5647058823529412,0.5647058823529412,0.5647058823529412))
    edit(p,'1 000',cost,'FntT400',16,fitz.TEXT_ALIGN_RIGHT,(0.2,0.2,0.2))
    
    return doc

def tink_tink_in(vr,cost,recvcon,bankcode,id):
    doc=fitz.open('d/tink-tink-in.pdf')
    p=doc[0]
    add_font(p,'FntT400','d\\fonts\\dsText\\400.ttf')
    add_font(p,'FntH400','d\\fonts\\dsHeading\\400.ttf')
    edit(p,'2-12-064-577-913',id,'FntH400',9,fitz.TEXT_ALIGN_LEFT)
    edit(p,'012064577913',bankcode,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'5404050596',recvcon,'FntH400',9,fitz.TEXT_ALIGN_RIGHT)
    edit(p,'01.03.2024 14:45:18',vr,'FntT400',8,fitz.TEXT_ALIGN_LEFT,(0.5647058823529412,0.5647058823529412,0.5647058823529412))
    edit(p,'300',cost,'FntT400',16,fitz.TEXT_ALIGN_RIGHT,(0.2,0.2,0.2))
    
    return doc

doc=tink_sbp_out('01.23.4567 89:01:23','1 000','ААБ БВВ','+7 (123) 456-78-90','ГГД ДЕЕ','ЖЖЖ ЗЗЗ','0-12-345-678-901')
#doc=tink_tink_out('01.23.4567 89:01:23','1 000 000','ААА БББ','+7 (123) 456-78-90','ВВВ ГГГ','0-12-345-678-901')
#doc=sbp_tink_in('01.23.4567 89:01:23','1 000 000','+7 (123) 456-78-90','012345678901','0-12-345-678-901')
#doc=tink_tink_in('01.23.4567 89:01:23','1 000 000','0123456789','012345678901','0-12-345-678-901')
doc.save("tink_spb_out_result.pdf")