Title: Contacto
page-order: 3


<form class="form" id="contactform" action="//formspree.io/juanmadog@gmail.com" method="POST">
    <fieldset class="field">
        <label class="label" for="name"><span class="label-content">Nombre*</span></label>
        <input class="input" type="text" name="name" placeholder="Nombre" required style="width: 50%;">
    </fieldset>
    <fieldset class="field">
        <label class="label" for="_replyto"><span class="label-content">Email*</span></label>
        <input class="input" type="email" name="_replyto" placeholder="example@domain.com" required style="width: 50%;">

    </fieldset>
    <fieldset class="field">
        <label class="label" for="message"><span class="label-content">Mensaje*</span></label>
        <textarea class="input" name="message" rows="6" placeholder="Mensaje" required style="width: 100%"></textarea>
    </fieldset>
    <input class="hidden" type="text" name="_gotcha" style="display:none">
    <input class="hidden" type="hidden" name="_subject" value="Mensaje desde juanmadog">
    <fieldset class="field">
        <input class="button submit" type="submit" value="Enviar">
    </fieldset>
</form>
