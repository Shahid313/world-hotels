let SelectedCityName = document.getElementById("CityName")
let Hotels = document.getElementById("Hotels")
let RoomsCapicityText = document.getElementById("rooms_capicit_text")
let RoomPriceText = document.getElementById("room_price")
let currency = document.getElementById('currency')


SelectedCityName.addEventListener("click", () => {
    let my_options = document.querySelectorAll(".old_options");
    
    let i;
    for(i=0; i<=my_options.length - 1; i++){
      my_options[i].remove()
    }
    
    fetch("http://127.0.0.1:5000/home/get_all_hotels", {
      method:'GET',
      headers:{
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
      }
    }).then((response) => {
      response.json().then(
        response => {
          response.map((location) => {
              console.log(location)
              if(location.city_name == SelectedCityName.value){
                const newOption = document.createElement("option");
                newOption.innerHTML = location.hotel_name;
                Hotels.appendChild(newOption);
                const attr = document.createAttribute("class");
                attr.value = "old_options";
                newOption.setAttributeNode(attr);
                
              }
            
            
          })
        }
      )
    })
    
  });

  let date = new Date();
  let day = date.getDay();
  let month = date.getMonth() + 1;

  const Priceattr = document.createAttribute("value");

  currency.addEventListener("change", () => {
    let PeakSeasonConvertedAmount;
    let OffPeakSeasonConvertedAmount;

        fetch("http://127.0.0.1:5000/home/get_all_hotels", {
      method:'GET',
      headers:{
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
      }
    }).then((response) => {
      response.json().then(response => {
        response.map((hotel) => {
          if(currency.value == "USD"){
            PeakSeasonConvertedAmount = Number(hotel.peak_season_room_price) * 1.6
            OffPeakSeasonConvertedAmount = Number(hotel.off_peak_season_room_price) * 1.6
          }else if(currency.value == "Euros"){
            PeakSeasonConvertedAmount = Number(hotel.peak_season_room_price) * 1.2
            OffPeakSeasonConvertedAmount = Number(hotel.off_peak_season_room_price) * 1.2
          }else if(currency.value == "QAR"){
            PeakSeasonConvertedAmount = Number(hotel.peak_season_room_price) * 4.5
            OffPeakSeasonConvertedAmount = Number(hotel.off_peak_season_room_price) * 4.5
          }else if(currency.value == "AED"){
            PeakSeasonConvertedAmount = Number(hotel.peak_season_room_price) * 4.5
            OffPeakSeasonConvertedAmount = Number(hotel.off_peak_season_room_price) * 4.5
          }else if(currency.value == "PKR"){
            PeakSeasonConvertedAmount = Number(hotel.peak_season_room_price) * 200
            OffPeakSeasonConvertedAmount = Number(hotel.off_peak_season_room_price) * 200
          }else if(currency.value == "INR"){
            PeakSeasonConvertedAmount = Number(hotel.peak_season_room_price) * 100
            OffPeakSeasonConvertedAmount = Number(hotel.off_peak_season_room_price) * 100
          }else if(currency.value == "VND"){
            PeakSeasonConvertedAmount = Number(hotel.peak_season_room_price) * 3000
            OffPeakSeasonConvertedAmount = Number(hotel.off_peak_season_room_price) * 3000
          }else if(currency.value == "NPR"){
            PeakSeasonConvertedAmount = Number(hotel.peak_season_room_price) * 150
            OffPeakSeasonConvertedAmount = Number(hotel.off_peak_season_room_price) * 150
          }else{
            PeakSeasonConvertedAmount = hotel.peak_season_room_price
            OffPeakSeasonConvertedAmount = hotel.off_peak_season_room_price
          }


          if(month >= 6 && month <= 9){
            Priceattr.value = PeakSeasonConvertedAmount
          }else if(month >= 3 && month <= 4){
            Priceattr.value = PeakSeasonConvertedAmount
          }else if(month == 1 && day >= 1 && day <= 10){
            Priceattr.value = PeakSeasonConvertedAmount
          }else if(month == 12 && day >= 13 && day <= 19){
            Priceattr.value = PeakSeasonConvertedAmount
          }else{
            Priceattr.value =OffPeakSeasonConvertedAmount
          }

          RoomPriceText.setAttributeNode(Priceattr);

        })
      })
    })      
  })
            

  Hotels.addEventListener("change", (e) => {
    fetch("http://127.0.0.1:5000/home/get_all_hotels", {
      method:'GET',
      headers:{
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
      }
    }).then((response) => {
      response.json().then(response => {
        response.map((hotel) => {
          if(hotel.hotel_name == e.target.value){
            RoomsCapicityText.innerHTML = 'Rooms Capicity ('+hotel.rooms_capicity+')';

            if(month >= 6 && month <= 9){
              Priceattr.value = hotel.peak_season_room_price
            }else if(month >= 3 && month <= 4){
              Priceattr.value = hotel.peak_season_room_price
            }else if(month == 1 && day >= 1 && day <= 10){
              Priceattr.value = hotel.peak_season_room_price
            }else if(month == 12 && day >= 13 && day <= 19){
              Priceattr.value = hotel.peak_season_room_price
            }else{
              Priceattr.value = hotel.off_peak_season_room_price
            }
            
            RoomPriceText.setAttributeNode(Priceattr);
          }
        })
      })
    })
  });

  
    