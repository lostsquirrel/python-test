# encoding: utf-8

study_template = u'''
<html>
<head>
<title>menuset</title>
<link type='text/css' rel="Stylesheet" href="css/tree.css" />
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<script type="text/javascript" src='js/jquery-1.9.1.min.js'></script>
<script type="text/javascript" src='menutree/menutree.js'></script>
<style type="text/css">
a.selected {
    color: #f95900;
}
.hidden {
    display:none;
}
</style>
<script type="text/javascript">
$(function(){
    $('.faisunMenu').on('click', 'a', function(){
        $('.faisunMenu').find('a.selected').removeClass('selected');
        $(this).addClass('selected')
    });
});
</script>
</head>
<body>
<script type="text/javascript">
    addtree('<b>学习</b>');
    %s
    createtree();
</script>
</body>
</html>

'''

practise_template = u'''
<html>
<head>
<title>menuset</title>
<link type='text/css' rel="Stylesheet" href="css/tree.css" />
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<script type="text/javascript" src='js/jquery-1.9.1.min.js'></script>
<script type="text/javascript" src='menutree/menutree.js'></script>
<style type="text/css">
a.selected {
    color: #f95900;
}
.hidden {
    display:none;
}
</style>
<script type="text/javascript">
$(function(){
    $('.faisunMenu').on('click', 'a', function(){
        $('.faisunMenu').find('a.selected').removeClass('selected');
        $(this).addClass('selected')
    });
});
</script>
</head>
<body>


<script type="text/javascript">
addtree('<B>练习</B>');
%s
createtree();
</script>
</body>
</html>
'''
