
      function getSelectedText(){
        let selectedText = '';

        if(window.getSelection){
            selectedText = window.getSelection();
        }else if (document.selection){
            selectedText = document.selection.createRange().text;
        }else return;

        if(selectedText == 'Aspirin'){
            document.querySelector('.popup').innerHTML = 'lorem lorem lorem lorem lorem lorem lorem lorem ';
            document.getElementById('pop').style.display="block"
        }else if(selectedText == ''){
           return null;
        }else{
            //alert(selectedText);
            document.querySelector('.popup').innerHTML = selectedText;
            document.getElementById('pop').style.display="block";
        }
        document.getElementById("pop").onclick = function(e){
            document.getElementById('pop').style.display="none";	
       }
    }
