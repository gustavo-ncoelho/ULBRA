const baseExpoente = (base, expoente) => {
    let resultado = 1;
    console.log(base+" ^ 0"+" = "+resultado);
    for (let i = 0; i < expoente; i++) {
      console.log(base+" ^ "+(i+1)+" = "+(resultado *= base));
    } 
    return "Muito obrigado!";
  };