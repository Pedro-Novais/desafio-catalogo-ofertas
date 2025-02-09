class InsertItens {
    URL = "http://127.0.0.1:8000/api/products"

    async get_products() {

        const response = await fetch(this.URL);
        const data = await response.json();

        if (!data || data.length == 0) {
            return this.no_items_find()
        }
        this.builder_list(data)

        new ListenEvents(data)
    }

    builder_list(products) {
        const container = document.querySelector('.containerProduct')
        for (let i = 0; i < products.length; i++) {
            this.builder_product(container, products[i])
        }
    }

    builder_product(container, item) {
        const card = document.createElement('div')
        card.setAttribute('class', 'productCard')

        this.builder_product_image(card, item.image)

        const attribute_container_info = [
            {
                type: 'class',
                value: 'containerInfo'
            }
        ]

        const card_info = this.create_element('div', attribute_container_info)

        this.builder_product_title(card_info, item.name)
        this.builder_product_price_full(card_info, item.price_full, item.price_with_discount)
        this.builder_product_price_final(card_info, item.price_full, item.price_with_discount, item.porcentage_discount)
        this.builder_product_instalments(card_info, item.instalments)
        this.builder_product_type_ship(card_info, item.type_ship_full)
        this.builder_product_ship_free(card_info, item.ship_free)
        this.builder_product_button(card_info, item.link)

        card.appendChild(card_info)
        container.appendChild(card)
    }

    builder_product_image(card, image) {
        const attributes_container = [
            {
                type: 'class',
                value: 'containerImage'
            }
        ]
        const container = this.create_element('div', attributes_container)

        const attributes_img = [
            {
                type: 'alt',
                value: 'Imagem'
            },
            {
                type: 'src',
                value: image
            }
        ]

        const img = this.create_element('img', attributes_img)

        container.appendChild(img)

        card.appendChild(container)
    }

    builder_product_title(card, title) {
        const attribute_container = [
            {
                type: 'class',
                value: 'line containerTitle'
            }
        ]

        const container = this.create_element('div', attribute_container)

        const title_product = this.create_element_default('p', title)

        container.appendChild(title_product)

        card.appendChild(container)
    }

    builder_product_price_full(card, price_full, price_final = null) {
        if (price_final) {
            const container_attributes = [
                {
                    type: 'class',
                    value: 'line containerPriceFull'
                }
            ]

            const container = this.create_element('div', container_attributes)

            const span = this.create_element_default('span', price_full)

            container.appendChild(span)

            card.appendChild(container)
        }
    }

    builder_product_price_final(card, price_full, price_final = null, porcentage_discount = null) {

        const container_attributes = [
            {
                type: 'class',
                value: 'line containerPriceFinal'
            }
        ]

        const container = this.create_element('div', container_attributes)

        if (price_final && porcentage_discount) {

            const p = this.create_element_default('p', price_final)
            const span = this.create_element_default('span', porcentage_discount)

            container.appendChild(p)
            container.appendChild(span)

            card.appendChild(container)
        }
        else {
            const p = this.create_element_default('p', price_full)

            container.appendChild(p)

            card.appendChild(container)
        }
    }

    builder_product_instalments(card, instalment = null) {
        if (instalment) {
            const container_attributes = [
                {
                    type: 'class',
                    value: 'line containerQuantitysIntalments'
                }
            ]

            const container = this.create_element('div', container_attributes)

            const p = this.create_element_default('p', instalment)

            container.appendChild(p)

            card.appendChild(container)
        }
    }

    builder_product_type_ship(card, type_ship = null) {
        if (type_ship == 1) {
            const container_attributes = [
                {
                    type: 'class',
                    value: 'line containerTypeShip'
                }
            ]

            const container = this.create_element('div', container_attributes)

            const span_attributes = [
                {
                    type: 'id',
                    value: 'full'
                }
            ]

            const span = this.create_element('span', span_attributes)

            const msg = "Entrega Full"

            span.innerHTML = msg

            container.appendChild(span)

            card.appendChild(container)
        }
    }

    builder_product_ship_free(card, ship_free = null) {
        if (ship_free) {
            const container_attributes = [
                {
                    type: 'class',
                    value: 'line containerShipFree'
                }
            ]

            const container = this.create_element('div', container_attributes)

            const msg = "Entrega grátis"

            const span_attributes = [
                {
                    type: 'id',
                    value: 'free'
                }
            ]

            const span = this.create_element('span', span_attributes)

            span.innerHTML = msg

            container.appendChild(span)

            card.appendChild(container)
        }
    }

    builder_product_button(card, link) {
        const container_attributes = [
            {
                type: 'class',
                value: 'line containerButtonProduct'
            }
        ]

        const container = this.create_element('div', container_attributes)

        const button_attributes = [
            {
                type: 'href',
                value: link
            },
            {
                type: 'target',
                value: '_blank'
            },
            {
                type: 'rel',
                value: 'noopener noreferrer'
            }
        ]

        const button = this.create_element('a', button_attributes)

        button.innerHTML = "Acessar Produto"

        container.appendChild(button)

        card.appendChild(container)


    }

    create_element(type, attributes = null) {
        const div = document.createElement(type)

        if (attributes) {
            for (let i = 0; i < attributes.length; i++) {
                const type_attribute = attributes[i].type
                const value_attribute = attributes[i].value

                div.setAttribute(type_attribute, value_attribute)
            }
        }

        return div
    }

    create_element_default(type, value) {
        const element = document.createElement(type)

        element.innerHTML = value

        return element
    }

    no_items_find() {
        const main = document.querySelector('main')

        const container_attributes = [
            {
                type: 'class',
                value: 'anyItens'
            }
        ]
        const container = this.create_element('div', container_attributes)

        const msg = "Nenhum item foi encontrado :("
        const h1 = this.create_element_default('p', msg)

        container.appendChild(h1)

        main.appendChild(container)
    }
}

class ListenEvents {
    constructor(product_json = null) {
        const products = document.querySelectorAll('.productCard')

        const filter_select = document.querySelector('#filter')

        filter_select.addEventListener('change', (event) => {
            this.reset_filter(products)
            this.filter_items(products, event.target.value, product_json)
        })
    }

    filter_items(products, type, product_json) {
        if (type == "all") {
            products.forEach(element => {
                element.style.display = 'unset'
            });
        }
        else if (type == "ship_free") {
            products.forEach(element => {
                const ship_free = element.querySelector('#free')

                if (!ship_free) {
                    element.style.display = 'none'
                }
            });
        }
        else if (type == "ship_full") {
            products.forEach(element => {
                const ship_full = element.querySelector('#full')

                if (!ship_full) {
                    element.style.display = 'none'
                }
            });
        }
        else if (type == "max_prices") {
            const new_product_max = product_json.sort((a, b) => b.price - a.price);

            if (new_product_max) {
                this.clean_products()
                new InsertItens().builder_list(new_product_max)
                new ListenEvents()
            }
        }
        else if (type == "min_prices") {
            const new_product_min = product_json.sort((a, b) => a.price - b.price);

            if (new_product_min) {
                this.clean_products()
                new InsertItens().builder_list(new_product_min)
                new ListenEvents()
            }
        }
        else if (type == "max_discount") {
            const new_discount_max = product_json.sort((a, b) => b.porcentage - a.porcentage);

            if (new_discount_max) {
                this.clean_products()
                new InsertItens().builder_list(new_discount_max)
                new ListenEvents()
            }
        }
    }

    reset_filter(products) {
        products.forEach(element => {
            element.style.display = 'unset'
        });
    }

    clean_products() {
        const products = document.querySelectorAll('.productCard')

        products.forEach(element => {
            element.remove()
        })
    }
}

new InsertItens().get_products()