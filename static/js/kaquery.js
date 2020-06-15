function CnfDelete(id)
{
    var request=new XMLHttpRequest();
    var url='/pod/delete/' + id;
    alert(url);
    request.onreadystatechange=function(){
        
        if(this.readyState==4 && this.status==200){
            alert(this.responseText);
            if(this.responseText=="1"){
                alert("Record Deleted");
                document.getElementById(id).remove();
            } else{
                alert("No Record found.");
               // window.reload();
            }
            
        }
    };
    request.open("GET",url,true);
    request.send();
}