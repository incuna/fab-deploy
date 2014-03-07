# fab-django-deploy

Fabric tasks to help deploying and updating django sites.

## Installation

    pip install fab-django-deploy
    

Create a `fabfile.py`

    from fabric.api import env

    import fab_deploy


    env.host_string = 'project_name.incunatesting.com'
    env.user = 'incuna'
    env.site_path = '/var/www/project_name.incunatesting.com/'
    

Run `fab -ls` to see a list of commads
    
>Available commands:
>
>    fab_deploy.manage      Run a django management command. e.g. fab_deploy.manage:syncdb
>    fab_deploy.pip         Run pip install.
>    fab_deploy.pull        Run git pull.
>    fab_deploy.supervisor  Run a supervisorctl command. e.g. fab_deploy.supervisor:'restart all'
>    fab_deploy.update      Update the site folder.
