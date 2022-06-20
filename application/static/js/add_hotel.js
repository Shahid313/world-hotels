let AddHotelCityName = document.getElementById("AddHotelCityName")
let HotelRoomsCapicity = document.getElementById("HotelRoomsCapicity")
let HotelOffPeakSeasonRate = document.getElementById("HotelOffPeakSeasonRate")
let HotelPeakSeasonRate = document.getElementById("HotelPeakSeasonRate")

AddHotelCityName.addEventListener("change", () => {
    const attr = document.createAttribute("value");
    const attr2 = document.createAttribute("value");
    const attr3 = document.createAttribute("value");
    console.log(AddHotelCityName.value)
    if(AddHotelCityName.value == "Amsterdam"){
      attr.value = 100;
      attr2.value = 80;
      attr3.value = 150;
    }else if(AddHotelCityName.value == "Athens"){
      attr.value = 100;
      attr2.value = 60;
      attr3.value = 120;
    }else if(AddHotelCityName.value == "Berlin"){
      attr.value = 120;
      attr2.value = 70;
      attr3.value = 140;
    }else if(AddHotelCityName.value == "Madrid"){
      attr.value = 130;
      attr2.value = 60;
      attr3.value = 160;
    }else if(AddHotelCityName.value == "Vienna"){
      attr.value = 70;
      attr2.value = 70;
      attr3.value = 140;
    }else if(AddHotelCityName.value == "Paris"){
      attr.value = 80;
      attr2.value = 80;
      attr3.value = 130;
    }else if(AddHotelCityName.value == "Edinburgh"){
      attr.value = 110;
      attr2.value = 70;
      attr3.value = 170;
    }else if(AddHotelCityName.value == "Rome"){
      attr.value = 120;
      attr2.value = 80;
      attr3.value = 160;
    }else if(AddHotelCityName.value == "London"){
      attr.value = 150;
      attr2.value = 70;
      attr3.value = 220;
    }else if(AddHotelCityName.value == "Milan"){
      attr.value = 160;
      attr2.value = 80;
      attr3.value = 190;
    }else if(AddHotelCityName.value == "Geneva"){
      attr.value = 100;
      attr2.value = 80;
      attr3.value = 130;
    }else if(AddHotelCityName.value == "Sofia"){
      attr.value = 90;
      attr2.value = 50;
      attr3.value = 110;
    }else if(AddHotelCityName.value == "Dubai"){
      attr.value = 100;
      attr2.value = 90;
      attr3.value = 150;
    }else if(AddHotelCityName.value == "Islamabad"){
      attr.value = 90;
      attr2.value = 50;
      attr3.value = 70;
    }else if(AddHotelCityName.value == "Mumbai"){
      attr.value = 100;
      attr2.value = 50;
      attr3.value = 90;
    }else if(AddHotelCityName.value == "Kathmandu"){
      attr.value = 80;
      attr2.value = 50;
      attr3.value = 70;
    }else if(AddHotelCityName.value == "Hanoi"){
      attr.value = 80;
      attr2.value = 50;
      attr3.value = 70;
    }else if(AddHotelCityName.value == "Doha"){
      attr.value = 100;
      attr2.value = 90;
      attr3.value = 130;
    }else if(AddHotelCityName.value == "Budapest"){
      attr.value = 100;
      attr2.value = 60;
      attr3.value = 130;
    }else if(AddHotelCityName.value == "Brussels"){
      attr.value = 90;
      attr2.value = 80;
      attr3.value = 190;
    }else if(AddHotelCityName.value == "Prague"){
      attr.value = 110;
      attr2.value = 70;
      attr3.value = 180;
    }else if(AddHotelCityName.value == "Copenhagen"){
      attr.value = 100;
      attr2.value = 70;
      attr3.value = 130;
    }else if(AddHotelCityName.value == "Helsinki"){
      attr.value = 100;
      attr2.value = 70;
      attr3.value = 120;
    }else if(AddHotelCityName.value == "Stockolm"){
      attr.value = 110;
      attr2.value = 70;
      attr3.value = 140;
    }
  
    HotelRoomsCapicity.setAttributeNode(attr);
    HotelOffPeakSeasonRate.setAttributeNode(attr2);
    HotelPeakSeasonRate.setAttributeNode(attr3);
  });