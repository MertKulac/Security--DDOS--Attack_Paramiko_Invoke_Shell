def SendMailwAttachment_(List_, Ek):
    from email import encoders
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    import os

    ServerIP_, Port_ = "10.218.130.60", 25

    # /// MAIL DEĞİŞKENLER
    From_ = "TEST@smtp.test.com"
    FromAlias_ = "TEST"
    To_ = ["mertkulac@test.com"]
    cc_ = ["mertkulac@test.com"]
    Subject_ = "DDOS 2.0 Customer Announce Control"
    AttachmentList_ = [Ek]

    Table_ = "<tr>" + "</tr><tr>".join("<td>" + "</td><td>".join(x) + "</td>" for x in List_) + "</tr>"

    MailText_ = """\
            <p>Hello,</p>
            <p>Suspected DDOS announcement has been detected in following IPs which are protected by DDOS 2.0 on Arbor. </p>
            <p>Best Regards </p>
            <table border="1" cellpadding="1" cellspacing="1" style="width:500-700px">
                <tbody>
                    %s 
                </tbody>
            </table>
            <p>&nbsp;</p>

                        """ % Table_

    # /// FUNCTION MAIN BODY /// DO NOT CHANGE
    Mail_ = MIMEMultipart('alternative')
    Mail_['To'] = ", ".join(To_)
    Mail_['Bcc'] = ", ".join(To_)
    Mail_['cc'] = ", ".join(cc_)
    Mail_['From'] = FromAlias_
    Mail_['Subject'] = Subject_
    Mail_.preamble = 'Need HTML reader!!\n'

    MailBodyPart_ = MIMEText(MailText_, 'html')
    Mail_.attach(MailBodyPart_)

    if len(AttachmentList_) != 0:
        for EachFile_ in AttachmentList_:
            try:
                with open(EachFile_, 'rb') as fp:
                    AttachmentPart_ = MIMEBase('application', "octet-stream")
                    AttachmentPart_.set_payload(fp.read())
                encoders.encode_base64(AttachmentPart_)
                AttachmentPart_.add_header('Content-Disposition', 'attachment', filename=os.path.basename(EachFile_))
                Mail_.attach(AttachmentPart_)
            except Exception as e:
                print("INFO! Dosya ekleme hatası : %s" % e)

    FullMail_ = Mail_.as_string()
    with smtplib.SMTP(ServerIP_, Port_) as Connection_:
        Connection_.sendmail(From_, To_, FullMail_)
        Connection_.close()
