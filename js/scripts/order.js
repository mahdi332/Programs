const select_option = document.getElementById("order_name");
const ezafe_btn = document.getElementById("thebtn");
const tedad = document.getElementById("order_count");
const tab_body = document.getElementById("tab_body");
// values
const op_arr = [
  { name: "چای ساده", price: 5 },
  { name: "چای ماسالا", price: 25 },
  { name: "چای سبز", price: 30 },
  { name: "اسپرسو", price: 16 },
  { name: "لانگ بلک", price: 20 },
  { name: "لاته", price: 18 },
  { name: "آمریکانو", price: 22 },
  { name: "کاپوچینو", price: 26 },
];
let count = 0;
let options = "<option>انتخاب کنید...</option>";
for (let i = 0; i < op_arr.length; i++) {
  options += `<option>${op_arr[i].name}</option>`;
  select_option.innerHTML = options;
}
// end values

// events
ezafe_btn.addEventListener("click", remplier);
// end of events
// functions
function remplier(val) {
  val.preventDefault();
  const product_name = select_option.value;
  const product_count = tedad.value;
  if (!product_name || !product_count) {
    return alert("لطفا تمامی فیلد ها را پر کنید");
  }
  const c = { name: product_name, count_price: product_count };
  selected_op.push(c);
  let price;
  price = op_arr.filter((val) => {
    if (val.name == product_name) {
      return val.price;
    }
  });
  tab_body.innerHTML += `
    <tr>
    <td>
    ${count + 1}
    </td>
    <td>
    ${product_name}
    </td>
    <td>
    ${product_count}
    </td>
    <td>
    ${price[0].price}
    </td>
    <td>
    ${price[0].price * product_count}
    </td>
    <td>
        <button id="delete_btn" onclick="remove(this)">del</button>
      </td>
    </tr>`;
  count++;
}
function remove(that) {
  that.parentNode.parentNode.remove();
}
