# ~azt
Now I think I should write down a plan about the azt so that I can start making
the azt packages and publish them, there maybe several important errors, so
that i can learn from them. ～azt should be something to help grow up my skills
and make me much more strong, this file itself I beleive should be managed in a
certain way so that I can manage it much more effeciently. 

The azt versioning should be clear. X.Y.Z.PatchNO.PlatformCode.BuildData.BuildCounter.
CHANGE: azt-X.Y.Z.PATCH.platformcode.prefix
X may never change in current situation. I will directly start X for 1 this
time.
Y will change when I add a bigger topic to the program or a new domain. For
example if I add some code to handle all django staff, then I add a dominate Y. 
Z is a new feature and all error handlings, small updates wont change z if I
did not published and released the package.
The program itself may update itself for some patches and that is how I change
when I made some bug fixes(not a new feature nor a new function nor a new class
of data something, patch is just a bug fix for finded staff)

For clearity,Platform code as follows: 
* Mac darwin-x64 (.pkg or .tar.gz) azt-1.0.0.0.darwin-x64.pkg azt-1.o.o.o.darwin-x64.tar.gz     
* Linux linux-64 (.tar.gz) azt-1.0.0.0.linux-x64.tar.xz
* Linux ARMv7 linux-armv7l (.tar.xz) azt-1.0.0.0.linux-armv7l.tar.xz
* Linux ARMv8 linux-arm64 (.tar.xz) azt-1.0.0.0.linux-arm64.tar.xz

## TODO ideas
- [ ] create a project directory to the project.
- [ ] create some of the builtin functionalities that are going to be free.
- [ ] think that how the packages would be hosted, installed and been used later.
- [ ] think that weather can others contribute to the project and how.
- [ ] `azt install <pkg>`
- [ ] `azt remove <pkg>`
- [ ] `azt update`
- [ ] `azt upgrade`
- [ ] `azt clean` 
- [ ] `azt doctor`

Now i have a new idea. just like `sudo apt install` or `sudo apt remove` the `azt` is same as `sudo` and `apt` can be some words like `pkg` so it canbe a `pkg` named pkg that handles all the package staff like 
* azt pkg install <'pkg'>
* azt pkg remove <'pkg'>


The code itself should have the ability to update and upgrade from the source.

How we can authenticate? should the packages be listed and stored in a server so that we have to buy a server? I don't think so. Then I mean we can just authenticate the legibility of the azt itself by cheaking weather the user machine ID is the same as we have generated for them ( they have to buy a copy, oh ..... that means we need a server to do that)

Everytime user uses a azt function, we may need to `check the internet connection` and then `if the connection is ok` then we need to check the user is allowed to use or not the software.

Another idea is user have to subscribe so we can just test the user data (machine time?) maybe we should do that and just test weather user time is autdated. (save it into somewhere in a file or a database, maybe we should use a data base and it should check the data base authentication)

the data base is created by a machine and only that machine can open ( i think there should be some id's like machine network card, wifi or machine id or use all of them as a user id )


Everything is a package object in azt. and we should manage it just like that.(just a file also a pkg?)

a pkg should at least have one `__init__.azt` file. we can search for this file to check weather it is a pkg or just a normal directory.

can we use one of the azt pkg in another one? 
yes we can we should able to transfer data or objectss from one to another. 


## changelog
changelogs should be written here. (Including release notes)


# To-Do
- [ ] code check internet
- [ ] code check ip 
- [ ] code check mac id 
- [ ] code generate uniq machine id
- [ ] code read azd data
- [ ] code write to azd data
- [ ] code run azx code ?
- [ ] get machine time
- [ ] get timezone
- [ ] get machine language
- [ ] get username
- [ ] get platform os and other specifications
- [ ] get installed python version
- [ ] get installed python packages list




ok, I understand what to do. 

The ~azt  version 1 Not has a package installation idea and all the pkgs are provided offically.

~azt 2 supports pkg installation. 




HOW to use ? 

`azt`

informations about the azt program, should written very dummy, use sys.argv[]

printout azt in current way1
check the OS language and print out the message in correspondin OS language.

reads the current user, corrent user location, and current user time, greets user.

Hi Azat from Kazakhstan! Thanks for Using ~azt.
Here are some informations which may help you to start:


`azt --short or -s`
just a AzatAI that's all.

`azt doctor`
`azt -s` + internet connectivity, current system version, current registered user info, activated copy ? when will be out of data? license valid? 
check azt's directory permissions.
all the files with in the packages should be executable.

`azt help`
you need to give me some pkg name to show the help info.

`azt help pkg`

show the pkg's help info. it is stored within the pkg directory in a markdown file named pkgname.md




maybe we are not going to use the click ?
or maybe we just use it for the pkgs? not for the main project?



 azt/
 install.sh
 