const data = {
    "Post-1": {
      userId: 1,
      id: 1,
      title:"sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        ,
      body:`quia et suscipit\nsuscipit recusandae consequuntur expedita et
    cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt re   eveniet architecto`,
    },
  
    "Post-2": {
      userId: 2,
      id: 2,
      title: "qui est esse",
      body: `est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores
   neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non
   debitis possi`,
    },
    "Post-3": {
      userId: 3,
      id: 3,
      title: "ea molestias quasi exercitationem repellat qui ipsa sit aut",
      body: `et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem
   doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"`,
    },
    "Post-4": {
      userId: 4,
      id: 4,
      title: "eum et est occaecati",
      body: `ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda
   provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam
   iure\nquis su`,
    },
  };
  
  // const newData = []
  // newData.push(data)
  // console.log(data)
  // objectReference = {
  //   dataInfo1: data["Post-1"],
  //   dataInfo2: data["Post-2"],
  //   dataInfo3: data["Post-3"],
  //   dataInfo4: data["Post-4"],
  // }
  arrayReference = [
    data["Post-1"],
    data["Post-2"],
    data["Post-3"],
    data["Post-4"],
  ]
  
  function constructIterator(arrayElement){
    let startIndex = 0;
    return {
      next : function(){
        if(startIndex < arrayElement.length){
          return {
            value:arrayElement[startIndex++],
            done:false
          }
        }else
        {
          return{
            done:true
          }
        }
      } 
    }
  }
  
  const getObject = constructIterator(arrayReference)
  nextChange()
  const selectBtn = document.querySelector('.iterator_button')
  selectBtn.addEventListener('click', nextChange)
  
  function nextChange(){
    const getValue = getObject.next().value;
    if (getValue === undefined){
      document.body.innerHTML = `
      <div class = "newDiv">
      <h1 class = "finish">Done Iterators</h1>
      <p class = "paraFinish">
      Reload in 3 seconds
      </p>
      <div class = "loader"></div>
      </div>`
  
      setTimeout(function(){
        window.location.reload()
      }, 3000)
    }
    else{
      let selectElement = document.querySelector('.card')
      selectElement.innerHTML = `
      <h1 class="card_heading">User-Id ${getValue.id}</h1>
      <p class="card_title">
        <span>Title</span>
        ${getValue.title}
      </p>
      <p class="card_body">
        <span>Body</span>
        ${getValue.body}
      </p>`
    }
  }
  
  function getHtmlonGenerator(getnewGenValue){
    if (getnewGenValue === undefined){
      document.body.innerHTML = `
      <div class = "newDiv">
      <h1 class = "finish">Done Iterators</h1>
      <p class = "paraFinish">
      Reload in 3 seconds
      </p>
      <div class = "loader"></div>
      </div>`
  
      setTimeout(function(){
        window.location.reload()
      }, 3000)
    }
    else{
      let selectElement = document.querySelector('.card_2')
      selectElement.innerHTML = `
      <h1 class="card_heading">User-Id ${getnewGenValue.id}</h1>
      <p class="card_title">
        <span>Title</span>
        ${getnewGenValue.title}
      </p>
      <p class="card_body">
        <span>Body</span>
        ${getnewGenValue.body}
      </p>`
    }
  }
  
  function newNextChange(){
    function* newChange(){
      // let i =0
      yield data["Post-1"]
      yield data["Post-2"]
      yield data["Post-3"]
      yield data["Post-4"]
    }
    const gen = newChange()
    const getnewGenValue = gen.next().value;
    getHtmlonGenerator(getnewGenValue)
  
  }
  
  function* newChangeGenerate(){
    // let i =0
    yield data["Post-1"]
    yield data["Post-2"]
    yield data["Post-3"]
    yield data["Post-4"]
  }
  const general = newChangeGenerate()
  
  console.log(general.next())
  console.log(general.next())
  console.log(general.next())
  console.log(general.next())
  console.log(general.next())
  
  genrateBtn = document.querySelector('.generator_button')
  genrateBtn.addEventListener('click', newNextChange)
  // const gen = numberGen()
  // console.log(gen.next().value.userId)
  // console.log(gen.next())
  // console.log(gen.next())
  // console.log(gen.next())
  // console.log(gen.next())
  // console.log(gen.next())
  // console.log(gen.next())
  