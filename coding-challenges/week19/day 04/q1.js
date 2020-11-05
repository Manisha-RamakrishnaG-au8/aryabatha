document.addEventListener("keydown", KeyCheck);  //or however you are calling your method
function KeyCheck(event)
{
   var KeyID = event.keyCode;
   switch(KeyID)
   {
      case 8:
      alert("backspace");
      break; 
      case 46:
      alert("delete");
      break;
      default:
      break;
   }
}
