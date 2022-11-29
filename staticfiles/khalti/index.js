import KhaltiCheckout from "khalti-checkout-web";

let config = {
  publicKey: "live_public_key_813c5bbe896d4cae9716d7ca4bb1e118",
  productIdentity: "54s5af45",
  productName: "Fool would buy",
  productUrl: "http://Xina.com.np",
  eventHandler: {
    onSuccess(payload) {
      // hit merchant api for initiating verfication
      console.log(payload);
    },
    // onError handler is optional
    onError(error) {
      // handle errors
      console.log(error);
    },
  },
  // one can set the order of payment options and also the payment options based on the order and items in the array
  paymentPreference: [
    "MOBILE_BANKING",
    "KHALTI",
    "EBANKING",
    "CONNECT_IPS",
    "SCT",
  ],
};

let checkout = new KhaltiCheckout(config);
let btn = document.getElementById("payment-button");
let total = +document.getElementById("grand_total_9860")?.innerText
console.log(total);
btn.addEventListener("click", () => checkout.show({ amount: total*100 }));