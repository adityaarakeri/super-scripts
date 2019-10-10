from jinja2 import Environment, FileSystemLoader


def template_loader(template_name='', template_folder='', **kwargs):
    '''
        The Function loads any html template using Jinja

        Args:
            template_name
            template_folder
            additional_arguments

        return:
            template string
    '''
    file_loader= FileSystemLoader(template_folder)
    env = Environment(loader=file_loader)

    template = env.get_template(template_name)
    return template


# example
if __name__ == "__main__":
    print(template_loader(template_name='email.html',template_folder='',name= 'Arkadip'))