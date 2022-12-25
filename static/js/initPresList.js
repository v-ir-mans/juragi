function addPresent(name, num) {
    $('#presents_list').prepend(`<li class="list-group-item" id="${num}">
        <div class="row">
            <div class="col-12 col-lg-9" style="margin-bottom: 13px;">
                <ul class="list-group">
                    <li class="list-group-item"><span>Vārds: ${name}</span></li>
                    <li class="list-group-item"><span>Numurs: ${num}</span></li>
                </ul>
            </div>
            <div class="col text-end align-self-center">
            <button id="${num}" onClick="deleteItem(this.id)" class="btn btn-danger">ATCELT</button>
            </div>
        </div>
    </li>`); 
}

