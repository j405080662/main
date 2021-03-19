import {
	ajaxRequest
} from './ajaxRequest.js'; //引入服务器地址;
// 动态实现radio选中触发事件
// $('input:radio[name="role"]').click(function(){
// 	var checkValue = $('input:radio[name="role"]:checked').val();
// 	alert(checkValue);
// });
//


//
// $(':submit').click(function(){
// 	alert('1111');
// 	let account = $('input[type="tel"]').val();
// 	let email = $('input[type="email"]').val();
// 	let name = $('input[name="name"]').val();
// 	let sex = $('input:radio[name="sex"]:checked').val();
// 	let birthday = $('input[type="date"]').val();
// 	let passWord = $('input[type="password"]').val();
// 	let passWordRepet = $('input[name="passWord"]').val();
// 	console.log(name)
// 	var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
// 	if(!account || !email && !reg.test(email) || !name || !birthday ||!passWord){
// 		return
// 	}
// 	$.ajax({
//                                     url:'http://127.0.0.1:5000/confirm',
//                                     data:{
//
//                                         name:name,
//                                         au:au,
//                                         classify:classify,
//                                         wordcount:wordcount,
//                                         all_recomm:all_recomm,
//                                         click:click,
//                                         weekrecomm:weekrecomm
//                                         },
//                                     dataType:'json',
//                                     method:'POST',
//                                     success:function(res){
//                                         console.log(res)
//                                         location.reload()
//
//                                     }
// 	// ajaxRequest({
// 	// 	url: "/keshihua",
// 	// 	method: "POST",
// 	// 	param: {
// 	// 		account:account,
// 	// 		email:email,
// 	// 		name:name,
// 	// 		sex:sex,//male:男，female:女
// 	// 		birthday:birthday, //格式:2021-02-04
// 	// 		password:passWord,
// 	// 	},
// 	// 	successBack: (res) => {
// 	// 		console.log(res)
// 	// 	}
// 	});
// });

