const encipher_title=document.getElementById("encipher-title"),decipher_title=document.getElementById("decipher-title"),encipher_input=document.getElementById("encipher-input"),encipher_output=document.getElementById("encipher-output"),decipher_input=document.getElementById("decipher-input"),decipher_output=document.getElementById("decipher-output"),encipher_copy=document.getElementById("encipher-copy"),decipher_copy=document.getElementById("decipher-copy"),encipher_clear=document.getElementById("encipher-clear"),decipher_clear=document.getElementById("decipher-clear");function copyEncipher(e){var c=!1;if(document.body.createTextRange)(t=document.body.createTextRange()).moveToElementText(encipher_output),t.select(),document.execCommand("Copy"),c=!0;else if(window.getSelection){var t,n=window.getSelection();(t=document.createRange()).selectNodeContents(encipher_output),n.removeAllRanges(),n.addRange(t),document.execCommand("Copy"),c=!0}c&&(encipher_copy.value="copied!",setTimeout(function(){encipher_copy.value="copy"},3e3))}function copyDecipher(e){var c=!1;if(document.body.createTextRange)(t=document.body.createTextRange()).moveToElementText(decipher_output),t.select(),document.execCommand("Copy"),c=!0;else if(window.getSelection){var t,n=window.getSelection();(t=document.createRange()).selectNodeContents(decipher_output),n.removeAllRanges(),n.addRange(t),document.execCommand("Copy"),c=!0}c&&(decipher_copy.value=ec("copied!"),setTimeout(function(){decipher_copy.value=ec("copy")},3e3))}function updateEncipher(e){encipher_output.innerHTML=ec(e.target.value)}function updateDecipher(e){dc(e.target.value)}function clearEncipher(e){encipher_output.innerHTML="",encipher_input.value="",encipher_clear.value="cleared!",setTimeout(function(){encipher_clear.value="cleared"},3e3)}function clearDecipher(e){decipher_output.innerHTML="",decipher_input.value="",decipher_clear.value=ec("clear!"),setTimeout(function(){decipher_clear.value=ec("clear")},3e3)}encipher_title.innerHTML="EnterTextToEnCipher",decipher_title.innerHTML=ec("EnterTextToDeCipher"),encipher_copy.value="copy",decipher_copy.value=ec("copy"),encipher_clear.value="clear",decipher_clear.value=ec("clear"),encipher_input.addEventListener("input",updateEncipher),decipher_input.addEventListener("input",updateDecipher),encipher_copy.addEventListener("click",copyEncipher),decipher_copy.addEventListener("click",copyDecipher),encipher_clear.addEventListener("click",clearEncipher),decipher_clear.addEventListener("click",clearDecipher);