function fun_one():any
{
    return fun_two();
}
function fun_two():string
    {
        return "welcome";
    }
document.write(fun_one+"<br>");
document.write(fun_one());