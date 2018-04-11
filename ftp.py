from ftplib import FTP
timeout=20
port=21
ftp=FTP()

enbid=open('E:\\zhanghao\\enb_id.txt').read().splitlines()
print(enbid)

localpath='E:\\zhanghao\\'
remotepath='zhanghaoNEW\\ZIGONG-MDT\\test\\'

ftp.connect('192.168.17.189',port,timeout)
ftp.login('fast','fast*123')
print(ftp.getwelcome())
ftp.cwd(remotepath)
floderlist=ftp.dir()
for x in range(len(enbid)):
    try:
        ftp.cwd(str(enbid[x]))
        gz=ftp.nlst()
        print(gz)
        for filename in gz:
            print(filename)
            f = open(localpath + filename, 'wb')
            ftp.retrbinary('RETR %s' % filename, f.write)
        ftp.cwd('..')
    except:
        continue





















'''for filename in list:
    print(filename)
    f=open(localpath+filename,'wb')
    ftp.retrbinary('RETR %s'% filename,f.write)'''


