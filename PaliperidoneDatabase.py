import LightLinter as LL
import ttk
#import Refsi
import pickle as PI

CurAttr = {0:0}

TK = LL.TK

fi = open('SL.li', 'rb')
SL = PI.load(fi)
fi.close()

fi = open('AT.li', 'rb')
AT = PI.load(fi)
fi.close()

##fi = open('FRAMES.li', 'rb')
##FRAMES = PI.load(fi)
##fi.close()

def DumpSL():

    fi = open('SL.li', 'wb')
    PI.dump(SL, fi)
    fi.close()

    print 'Saving the data: done'
    
def FillSemblocks():

    Ol = []
    for k, v in SL.items():
        si = k.strip()
        if si == '':
            continue
        ol = [len(v), si]
        Ol.append(ol)

    Ol.sort()
    Ol.reverse()

    for oline in Ol:
        lxline = str(oline[0])+'__'+oline[1]
        LL.TKDI['lx']['sb'].insert(TK.END, lxline) 

def reflect__sb(event):

    LL.TKDI['lx']['slots'].delete(0, TK.END)
    pair  = LL.reflect__lx__in__entry('sb')
    semblock = pair[1].split('__')[1]
    all_data = SL[semblock]
    SlotsLI = all_data.keys()
    SlotsLI.sort()
    for slot in SlotsLI:
        LL.TKDI['lx']['slots'].insert(TK.END, slot)

    all_attrs = AT[semblock]
    all_attrs.sort()
    LL.Fill__lx(all_attrs, 'attrs')
        
##    for attr in ks_li:
##        value = all_data[attr]
##        lx_line = attr+' :  '+value
##        LL.TKDI['lx']['attrs'].insert(TK.END, lx_line)
        
def reflect__slot(event):

    LL.TKDI['lx']['data'].delete(0, TK.END)
    pair  = LL.reflect__lx__in__entry('slots')
    slot = pair[1]
    sb = LL.TKDI['en']['sb'].get()
    semblock = sb.split('__')[1]
    slot_data = SL[semblock][slot]
    AttrsLI = slot_data.keys()
    AttrsLI.sort()
    for attr in AttrsLI:
        value = slot_data[attr]
        lx_line = attr+' :  '+value
        LL.TKDI['lx']['data'].insert(TK.END, lx_line)
        
def reflect__data(event):

    cs = int(LL.TKDI['lx']['data'].curselection()[0])
    CurAttr[0] = cs
    line = LL.TKDI['lx']['data'].get(cs)
    sl = line.split(' :')
    attr = sl[0]
    cur_value = sl[1].strip()
    if attr in SL:
        slots = SL[attr].keys()
        slots.sort()
        try:
            LL.TKDI['cb']['attribute']['values'] = slots
            LL.TKDI['la']['attribute']['text'] = attr
            LL.TKDI['cb']['attribute'].set(cur_value)
        except:
            pass
                    
        
def reflect_cb_attr():##event):

    value =   LL.TKDI['cb']['attribute'].get()
    attr = LL.TKDI['la']['attribute']['text']
    cs = CurAttr[0]
    LL.TKDI['lx']['data'].delete(cs)
    lx_line = attr +' :  '+value
    LL.TKDI['lx']['data'].insert(cs, lx_line)

    sb = LL.TKDI['en']['sb'].get()
    semblock = sb.split('__')[1]

    slot =  LL.TKDI['en']['slots'].get()
    SL[semblock][slot][attr] = value
    
    print 'reflect_cb_attr: done'

def reflect__attr(event):

    pair = LL.reflect__lx__in__entry('attrs')
    attr = pair[1]
    SlotsLI = SL[attr].keys()
    SlotsLI.sort()
    LL.TKDI['lx']['attr_slots'].delete(0, TK.END)
    LL.Fill__lx(SlotsLI, 'attr_slots')
        
def IntroducePair():

    attr = LL.TKDI['en']['attrs'].get()
    value = LL.TKDI['en']['attr_slots'].get()

    attr = attr.strip()
    value = value.strip()

    ok = 0
    if value == '':
        print 'select attr!'
        ok = 1
    if value == '':
        print 'select value!'
        ok = 1
        
    if ok == 0:
        
        sb = LL.TKDI['en']['sb'].get()
        semblock = sb.split('__')[1]
        slot =  LL.TKDI['en']['slots'].get()
        SL[semblock][slot][attr] = value
        lx_line = attr+' :  '+value
        LL.TKDI['lx']['data'].insert(TK.END, lx_line)

        
        
    
def CreateForms():

    LL.Create__root('Paliperidone Database')
    LL.Add__one__frame(0, 'root', 1, 1)
    LL.Add__lx('sb',    0, 1, 1, 20, 7, 'Arial 14')
    LL.TKDI['lx']['sb'].bind('<KeyRelease>', reflect__sb)
    LL.TKDI['lx']['sb'].bind('<ButtonRelease>', reflect__sb)

    LL.Add__lx('slots', 0, 1, 2, 25, 7, 'Arial 14')
    LL.TKDI['lx']['slots'].bind('<KeyRelease>', reflect__slot)
    LL.TKDI['lx']['slots'].bind('<ButtonRelease>', reflect__slot)
    
    LL.Add__lx('data', 0, 1, 3, 45, 7, 'Arial 14')
    LL.TKDI['en']['data'].grid_forget()

    
    LL.Add__one__frame('attrs', 0, 2, 3)
    
    LL.Add__cb('attribute', 'attrs', 1,1, 20,'Arial 14')
    LL.TKDI['la']['attribute']['bd'] = 1
    LL.TKDI['la']['attribute']['relief'] = TK.FLAT
    
    LL.TKDI['lx']['data'].bind('<KeyRelease>', reflect__data)
    LL.TKDI['lx']['data'].bind('<ButtonRelease>', reflect__data)

    LL.Add__button('Accept', 'attrs', 1,3, 10, 'Accept')
    LL.TKDI['bu']['Accept']['command'] = reflect_cb_attr
#    LL.TKDI['cb']['attribute']['validate'] = 'key' ##command'] = reflect_cb_attr
    LL.Add__button('Dump_SL', 'attrs', 1,4, 10, 'Save Data')
    LL.TKDI['bu']['Dump_SL']['command'] = DumpSL


    LL.Add__one__frame(1, 'root', 2, 1)
    LL.Add__lx('frames',    1, 1, 1, 20, 7, 'Arial 14')

    all_frames = SL.keys()
    all_frames.sort()
    arr = []
    for si in all_frames:
        si = si.strip()
        if si == '':
            continue
        arr.append(si)
        
    LL.Fill__lx(arr, 'frames')

    LL.Add__lx('attrs',      1, 1, 2, 20, 7, 'Arial 14')
    LL.TKDI['lx']['attrs'].bind('<KeyRelease>', reflect__attr)
    LL.TKDI['lx']['attrs'].bind('<ButtonRelease>', reflect__attr)

    LL.Add__lx('attr_slots',    1, 1, 3, 30, 7, 'Arial 14')

    LL.Add__one__frame('slots', 1, 3, 4)
    LL.Add__button('IntroducePair', 'slots', 1, 1, 10, 'Introduce')
    LL.TKDI['bu']['IntroducePair']['command'] = IntroducePair

    

    
def StartFills():

#    CreateForms()    
    FillSemblocks()
    
def Start():
    
    CreateForms()
    StartFills()

    LL.TKDI['fr']['root'].mainloop()

Start()



    
