console.log('Hello world')
const copyUrls = [...document.getElementsByClassName('copy-btn')]
console.log(copyUrls)

let former = null

copyUrls.forEach(btn=> btn.addEventListener('click', ()=>{
    const imgUrl = btn.getAttribute('data-url')
    console.log(imgUrl)
    navigator.clipboard.writeText(imgUrl)
    btn.textContent = 'Copied'
    navigator.clipboard.readText().then(clipText=>{
        console.log(clipText)
        alert(`Copied ${clipText}`)
    })

    if (former){
        former.textContent='Copy'
    }
    former = btn
}))