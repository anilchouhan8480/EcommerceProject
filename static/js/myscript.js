$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

    // suppose the `id` attribute of element is `message_container`.
var message_ele = document.getElementById("alert");

setTimeout(function(){ 
   message_ele.style.display = "none"; 
}, 3000);
// Timeout is 3 sec, you can change it


function valida(){
    var mobil = document.getElementById("mob");
    var patter = /^\d{10}$/;
    if(mobil.value.match(patter)){
        return true
    }
    else{
        alert("enter 10 digit mobile number");
    }
}

function se(){
    document.getElementById("sub").disabled = false;
}

function dis(){
    $("input").removeAttr('disabled');
    $("select").removeAttr('disabled');
}

// $('.plus-cart').click(function(){
//     var id = $(this).attr("pid").toString();
//     var eml = this.parentNode.children[2]
//     console.log(id);
//     $ajax({
//         type :  "GET",,
//         url : "/pluscart",
//         data : {
//             prod_id : id
//         },
//         success : function(data){
//             console.log(data)
//             eml.innerText = data.quantity
//             document.getElementById("totalamount").innerText= data.totalamount


//         }
//     })
// })

// $('.minus-cart').click(function(){
//     var id = $(this).attr("pid").toString();
//     var eml = this.parentNode.children[2]
//     console.log(id);
//     $.ajax({
//         type :  "GET",,
//         url : "/minuscart",
//         data : {
//             prod_id : id
//         },
//         success : function(data){
//             console.log(data)
//             eml.innerText = data.quantity
//             document.getElementById("totalamount").innerText= data.totalamount


//         }
//     })
// })