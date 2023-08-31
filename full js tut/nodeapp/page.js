const express= require("express");

const mysql=require("mysql");

var status='';
var text='';


const conn=mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'Mohfaiz@543',
    database:'mysqljs',
});
conn.connect((error)=>{
    if(error){
        status="Mysql not connected please check your connection";
    }
    else{
        status="Mysql connected";
        conn.query("select * from jstut;",(err,data)=>{
            if(err){
                console.log(err);
            }
            else{
                //console.log(data);
                var strdata=JSON.stringify(data);
                //console.log(strdata);
                var value=JSON.parse(strdata);
                //console.log(value);
                value.forEach((element) => {
                    text+=`<tr>
                    <td>${element.sno}</td>
                    <td>${element.name}</td>
                    <td>${element.username}</td>
                    <td>${element.password}</td>
                    <td>${element.gender}</td>
                    </tr>`
                });
                //console.log(text);
            }
        });
    }
});

const app=express();

app.use(express.urlencoded());

app.get("/",(req,res,next)=>{
    res.send(`
    <h1>`+status+`</h1>
    <table border=1>
    <thead>
    <tr>
    <th>S.No</th>
    <th>Name</th>
    <th>Username</th>
    <th>Password</th>
    <th>Gender</th>
    </tr>
    </thead>
    <tbody id="tabledata">`+text+`
    </tbody>

    </table>
    `);
});
app.listen(8000);