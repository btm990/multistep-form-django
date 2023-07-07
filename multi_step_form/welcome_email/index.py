HTML_MESSAGE = '''
<!DOCTYPE htmlPUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
</head>
<body style="margin: 0; background-color: white;">
    
    <center style="width: 100%; table-layout: fixed; background-color: white;" class="wrapper">

<!-- TOP BORDER -->
        <table style="border-spacing: 0; padding: 0;" width="100%">
            <tr>
                <td height="4" style="background-color: hsl(243, 100%, 62%);"></td>
            </tr>
        </table>
        
        <table style="border-spacing: 0; font-family: Helvetica, Arial, sans-serifs; background-color: white; margin: 0 auto; width: 100%; max-width: 600px; border-spacing: 0; color: hsl(213, 96%, 18%);" class="main" width="100%">
        
<!-- ICON AND THANKS MESSAGE-->
            <tr style="text-align: center;">
                <td style="padding: 48px 0 26px">
                    <img style="padding: 0; display: block; margin: auto;" src="https://i.postimg.cc/ZnRQW5yj/Untitled.png" width="80px" height="80px" title="thank-you" alt="checkmark-thank-you">
                    <p style="font-weight: bold; font-size: 20px; margin: 16px 0 12px; color: hsl(213, 96%, 18%)">Thanks for your subscription</p>
                    <p style="color: hsl(231, 11%, 63%); font-size: 14px; margin: 8px 0 8px;">Date and time of subscription: </p>
                    <p style="color: hsl(243, 100%, 62%); font-weight: bold; font-size: 14px; margin: 8px 0 8px;">{date}</p>
                </td>
            </tr>

<!-- DIVIDER --> 
            <tr style="text-align: center;">
                <td height="1" style="background-color: hsl(229, 10%, 67%)"></td>
            </tr>

<!-- MAIN MESSAGE -->

            <tr>
                <td style="padding: 30px 0;">
                    <p style="color: hsl(231, 11%, 63%); font-size: 15px;">Hi {name}, </p>
                    <p style="color: hsl(231, 11%, 63%); font-size: 14px;">Thank you for subscribing to LoremGaming. Please find your subscription summary below. </p>
                </td>
            </tr>

<!-- SUMMARY TABLE -->
            
            <tr>
                <td style="padding: 0;">
                    <table style="border-spacing: 0; font-size: 14px; background-color: hsl(231, 100%, 99%); color: hsl(213, 96%, 18%); padding: 22px 18px; margin: 15px auto 30px ;" width="100%">
                        <th style="text-align: left; padding: 0 0 12px;">Order Summary</th>
                        
                        {htmlSummaryTable}

<!-- SUMMARY TABLE BORDER -->
                        <tr>
                            <td style="padding: 0 0 8px"></td>
                            <td style="padding: 0 0 8px"></td>
                        </tr>

                        <tr style="font-weight: bold; font-size: 14px;">
                            <td style="border-top: 1px solid hsl(231, 11%, 63%); padding: 12px 0 0;">Total (excl. VAT)</td>
                            <td style="border-top: 1px solid hsl(231, 11%, 63%); padding: 12px 0 0; text-align: right;">ZAR{Total:.2f}</td>
                        </tr>

                    </table>
                </td>
            </tr>

        </table>
    
    </center>
</body>
</html>
'''

TABLE_ROW = '''
<tr>
    <td style="padding: 0 0 4px; font-size: 13px;">
        {item} ({period})
    </td>
    <td style="padding: 0 0 4px; font-size: 13px; text-align: right;">
        ZAR{amount:.2f}
    </td>
</tr>
'''

def htmlTemplate(name, plan, planTotal, yearly, dateTime, billTotal, **kwargs):
    planRow = TABLE_ROW.format(item=("%s plan" % plan), period=yearly, amount=planTotal)
    addons = [TABLE_ROW.format(item=' '.join(key.split('_')[0:2]), period=yearly, amount=val*18.80) for key, val in kwargs.items() if val != 0]
    
    TABLE_ROWs = "\n".join([planRow, *addons])

    html = HTML_MESSAGE.format(date=dateTime, name=name, htmlSummaryTable=TABLE_ROWs, Total=billTotal) 
    return html
