import styles from "./CurrencyButton.module.css"

/* 
:currency:
  the current chosen currency
:type:
  string
:changeCurrency:
  function that change currency value on parent
:type:
  function
*/
function CurrencyButton ({currency,changeCurrency}) {

  // ToDo 10.1
  return (
    <div className={styles.bodyContainer}>

        
        <button onClick={()=>changeCurrency("USD")}
          className={currency === 'USD' ? styles.currencyButtonActive : styles.currencyButtonActive} 
          /*in the value */> USD </button>
        

        
         <button onClick={()=>changeCurrency("JPY")}  
          className={currency === 'JPY' ? styles.currencyButtonDefault : styles.currencyButtonDefault} 
          /*in the value */> JPY </button>
       

    </div>   
  );

}

export default CurrencyButton;
