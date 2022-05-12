import React from "react";
import "./styles.css";


export default function App() {
   let [over,setOver]=React.useState(false);

   let buttonstyle={
    backgroundColor:''
  }

  if (index+1 == showData.length) {
    return "///"
}

  if(over){
    return  showData[index].price - showData[index+1].price;
  }
  else{
    return "No comparison!"
  }

}