#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")
'''print("<h3>hello welcome to restaurant ")
print("please order your food </h3>")'''

###################################### main form menu ############################

menu='''<div  align="center" style="background-color:#2eb82e;">  <br> <br>
         <p style="font-size:20px; font-weight:bold;"> Welcome to Bikaner Snacks <br> Please order your food  </p>

         <form action='bill.py' target="blank"  >
         <table border='2px' width='' style="background-color:white;">
         <thead style="">
             <th width="155"> ITEMS </th>
             <th width="80"> PRICES </th>
             <th> QUANTITY </th>
         </thead>
         <tbody style="text-align:center;font-weight:bold;">
         <tr>
            <td> vadapav </td>
            <td><input type='checkbox' name='order' value=18> 18.00 </td>
            <td><input type='number' min='0' width="20" height='16' name='qty' placeholder="1" /> </td>
          </tr>
           <tr>
            <td> bhajipav </td>
            <td><input type='checkbox' name='order' value=16> 16.00 </td>
            <td><input type='number' min='0' width="20" height='16' name='qty' placeholder="1" /> </td>
          </tr>
           <tr>
            <td> samosa </td>
            <td><input type='checkbox' name='order' value=15> 15.00 </td>
            <td><input type='number' min='0' width="20" height='16' name='qty' placeholder="1" /> </td>
          </tr>
           <tr>
            <td> samosa pav </td>
            <td><input type='checkbox' name='order' value=20> 20.00 </td>
            <td><input type='number' min='0' width="20" height='16' name='qty' placeholder="1" /> </td>
          </tr>
          <tr>
            <td> masaladosa </td>
            <td><input type='checkbox' name='order' value=35> 35.00 </td>
            <td><input type='number' min='0' width="20" height='16' name='qty' placeholder="1" /> </td>
          </tr>
          <tr>
            <td> meduvada </td>
            <td><input type='checkbox' name='order' value=25> 25.00 </td>
            <td><input type='number' min='0' width="20" height='16' name='qty' placeholder="1" /> </td>
          </tr>
          <tr>
            <td> pav </td>
            <td><input type='checkbox' name='order' value=5> 5.00 </td>
            <td><input type='number' min='0' width="20" height='16' name='qty' placeholder="1" /> </td>
          </tr>
          <tr>
            <td> <b> choose from above </b></td>
            <td><input type='checkbox' name='order' value=0 checked="checked" style="display:none">  </td>
            <td><input type='number' min='0' width="20" height='16' name='qty' value=0  style="display:none"/> </td>
           
          </tr>
          <tr>
            <th> <button> total </button> </th> 
            <td> <p> </p> </td>
          </tr>
          </tbody>
         </table> <br>
         <span> <b>P.S.: Make sure you select atleast 1 quantity </b></span>
         <br><br>
         <input type='submit' value='order now'>   <br> <br>
         </form>
         </div>
         '''
print(menu)


abc='''<div align="center" style="background-color:#;">  <br> <br>
         <span style="border:2px dashed black; border-bottom:none;font-weight:bold; padding:5px; margin-bottom:2px;"> Welcome to Bikaner Snacks </span> <br>  <br> 
          <span style="border:2px dashed black; font-weight:bold;  padding:5px; margin:2px;"> Please order your food </span> <br>  <br>'''


