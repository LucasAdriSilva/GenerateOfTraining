function loading(x) {
    if (x == true) {
        document.getElementById('body-content').classList.add('d-none');
        document.getElementById('loading').classList.remove('d-none');
    }
    else {
        document.getElementById('body-content').classList.remove('d-none');
        document.getElementById('loading').classList.add('d-none');
    }
}

export async function apiGet(rota, bool) {
    bool? loading(true): loading(false)
    
    const response = await fetch(`/${rota}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (response.ok) {
        const data = await response.json();
        loading(false)
        return data;
    } else {
        throw new Error(`Erro na requisição: ${response.status}`);
    }

}

