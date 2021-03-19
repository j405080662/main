// export const ajaxRequest = function(opt){
//     var isdefult=opt.isdefult||"need";//判断是否需要这个函数来判断，还是在页面请求回来的数据回来之后判断;
//     console.log(opt)
//     $.ajax({
//         url:'http://127.0.0.1:5000'+opt.url,//数据的接口的路径
//         dataType:'json',
//         method: opt.type||"POST",//请求的方式  默认是
//         data:opt.param||"",//请求的参数  默认是空
//         async:opt.async||true,//是否是异步，默认是异步
//         timeout: 10000,
//         success: function(res) {
//              console.log(res);
//             /*opt.isLoading==undefined&&app.loading('hide');*///判断是否需要加载函数  我的加载函数封装在一个对象里面执行  根据自己的项目来判断加载动画
//             if(isdefult=="need"){//判断是否需要这个函数来判断，还是在页面请求回来的数据回来之后判断
//                 if(res.code==200){//根据自己的项目的返回来判断
//                     opt.successBack instanceof Function&&opt.successBack(res.data);//成功的函数，看自己项目传值
//                 }
//                 else{
//                     console.log(res.msg)
//                 }
//             }
//
//             else
//             {
//                 opt.successBack instanceof Function&&opt.successBack(res);
//             }
//      },
//         error: function(res){
//             console.log(res);
//         }
//     });
// };
// // get请求：
// // demoAjax({
// //   "url":"get/user"，
// //  "successBack":funtion(){//成功之后的一些处理}
// // })
// // post请求：
// // demoAjax({
// //   "url":"get/user"，
// //   "type":"post",
// //   "param":{"user":"xg"}
// //   "successBack":funtion(){//成功之后的一些处理}
// // })