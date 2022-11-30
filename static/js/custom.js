"use strict"
$(function(){ 
    // FADE IN / NAV ACTIVE START
    $(".bg-layer").on("scroll", function() {
        fadeIn();
    })
    let fadeIn = function(){
        let winHeight = window.innerHeight;
        // FADE IN
        $(".fadein").each(function(){
            var offset = $(this).offset();
            var posY = offset.top - $(window).scrollTop();
            if(posY < (winHeight * 0.8)){
                $(this).fadeIn()
                $(this).addClass("show")
            }
        })
    }
    let getTypes = function(search){
        $.ajax({
            url: "/priceComparison/getTypes/" + search, 
            success: function(response)
            {
                let html = ""
                console.log(response)
                response.forEach(item => html += "<option value='" + item.url + "'>"+ item.name + "</option>");
                $("#products").html(html);
            },
            error: function()
            {
                console.log("Error"); 
            }
          });
    }
    let getOffers = function(uri){
        $.ajax({
            method: "POST",
            url: "/priceComparison/getOffers", 
            data: {
                url: uri
            },
            success: function(response)
            {
                $("#offers .title").text(response[0].title);
                response.forEach(function(resp){
                    let url = resp.link;
                    let price = resp.product_price;
                    let currency = resp.currency;
                    let shop = resp.shop_name;
                    $("#offers ul").append('<li><a href="'+ url +'"><span class="price">' + price + '</span> <span class="currency">'+ currency +'</span> at <span class="shop">'+ shop +'</span></a></li>')                    
                })        
            },
            error: function()
            {
                console.log("Error"); 
            }
        });
    }

    let lastRequest = 0;
    let waiting = 0
    $("input[name=product]").on('keyup', function() {
        let search = $(this).val()
        if (search.length > 5){
            if (lastRequest + 200 < Date.now()){
                waiting++
                let index = waiting
                setTimeout(function(){
                    if (waiting == index) {             
                        waiting = 0
                        getTypes(search)
                        return
                    }else return;
                }, 200)
            }else {
                lastRequest = Date.now();
                getTypes(search)
            }
        }
    });

    // initial calls
    fadeIn()
    if ($("#offers")){
        let data = $("#offers").data('url');
        if (data != undefined) 
            getOffers(data)
    }
    $("input[name=product]").attr('list', "products")
    // FADE IN / NAV ACTIVE END
})
