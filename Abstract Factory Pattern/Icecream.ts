interface Icecream{
    get():string
}
class ChocoIcecream implements Icecream{
    public get(){
        return 'ChocoIcecream'
    }
}
class StrawberryIcecream implements Icecream{
    public get(){
        return 'StrawberryIcecream'
    }
}
class ButterscotchIcecream implements Icecream{
    public get(){
        return 'ButterscotchIcecream'
    }
}

interface IcecreamContainer{
     getContainedIcecream(icecream:Icecream):string
}


class cupContainer implements IcecreamContainer{

    public getContainedIcecream(icecream:Icecream){
        return 'Cup with '
    }

}

class coneContainer implements IcecreamContainer{
    public getContainedIcecream(icecream:Icecream){
        return 'Cone with '
    }
}
class stickContainer implements IcecreamContainer{
    public getContainedIcecream(icecream:Icecream){
        return `Stick container with ${icecream.get()}`
    }
}

abstract class IceCreamFactory{
    public abstract getIcecreamFactory():Icecream
    public abstract getContainerFactory():IcecreamContainer

    public getProduct(){
        const icecream =this.getIcecreamFactory()
        const container=this.getContainerFactory()
        return container.getContainedIcecream(icecream)

    }
}

class ChocoStickCart extends IceCreamFactory{
    public getIcecreamFactory(){
        return new ChocoIcecream()
    }
    public getContainerFactory(){
        return new stickContainer()
    }


}
const choc=new ChocoStickCart()
console.log(choc.getProduct())
