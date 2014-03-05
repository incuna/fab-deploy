# fab-django-deploy

Fabric tasks to help deploying and updating django sites.

## Installation

    pip install fab-django-deploy
    

Create a `fabfile.py`

    from fabric.api import env

    import deploy


    env.host_string = 'project_name.incunatesting.com'
    env.user = 'incuna'
    env.site_path = '/var/www/project_name.incunatesting.com/'
    

Run `fab -ls` to see a list of commads
    
>Available commands:
>
>    deploy.manage      Run a django management command. e.g. deploy.manage:syncdb
>    deploy.pip         Run pip install.
>    deploy.pull        Run git pull.
>    deploy.supervisor  Run a supervisorctl command. e.g. deploy.supervisor:'restart all'
>    deploy.update      Update the site folder.
