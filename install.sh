#!/bin/sh

# change administration with web2py app

start=$(date +%s)

case $HOSTNAME in
	(MacBook.local) 
		# remove existing app
		cd
		rm -rf ~/project/python/web2py/applications/administration

		# copy webapp
		cp -R ~/project/python/web2py/applications/welcome/ ~/project/python/web2py/applications/administration
		rsync -zavr ~/Cloud/MEGA/Git/web2py/administration ~/project/python/web2py/applications/
		rsync -zavur ~/Cloud/MEGA/Git/web2py/administration ~/project/python/web2py/applications/

		# install demo with python
		#python ~/project/python/web2py/web2py.py --nogui --no-banner -S administration -M -R ~/project/python/web2py/applications/administration/modules/administration_install_demo.py

		# install with python
		#python ~/project/python/web2py/web2py.py --nogui --no-banner -S administration -M -R ~/project/python/web2py/applications/administration/modules/administration_install.py

		# install demo with curl
		#curl http://127.0.0.1:8000/administration/install_demo

		# install with curl
		curl http://127.0.0.1:8000/administration/install

		# functional test
		python ~/project/python/web2py/web2py.py --nogui --no-banner -S administration -M -R ~/project/python/web2py/applications/administration/modules/administration_functional_test.py
		;;
	# others default or pythonanywhere
	(*)
		# make folders for appdata
		cd
		mkdir -p ~/appdata/databases
		mkdir -p ~/appdata/uploads
		mkdir -p ~/appdata/webapp

		# change permission for appdata folder
		chmod 777 -R ~/appdata/

		# backup database
		rsync -zavr ~/web2py/applications/administration/databases/administration.sqlite ~/appdata/databases/

		# backup uploads
		rsync -zavr ~/web2py/applications/administration/uploads/* ~/appdata/uploads/

		# backup webapp
		rsync -zavr ~/web2py/applications/administration ~/appdata/webapp/

		# remove existing web2py app
		rm -rf ~/web2py/applications/administration

		# upload web2py packed app through admin
		;;
esac

end=$(date +%s)
diff=$(( $end - $start ))

echo Duration = $diff Seconds
echo Finished at = `date +%Y-%m-%d\ %H:%M:%S`
