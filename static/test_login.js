document.getElementById("login").onclick=function()
{
  var word = document.getElementById("pwd").value;
  var value = 0
  for (var i=0;i<word.length;i++)
  {
    value += (i+1)*word.charCodeAt(i);
  }
  document.getElementById("pwd").value = (value + 14507)%100007;
}