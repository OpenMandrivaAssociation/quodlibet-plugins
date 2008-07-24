%define name	quodlibet-plugins
%define version	1.0
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Advanced, elegant jukebox style music player plugins
Version: 	%{version}
Release: 	%{release}

Source0:	http://www.sacredchao.net/~piman/software/%{name}-%{version}.tar.bz2
Source1:	google.py
Source2:	dl-quodlibet-plugins.sh
URL:		http://www.sacredchao.net/quodlibet/
License:	GPL
Group:		Sound
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python
Requires:	python >= 2.5
Requires:	quodlibet

%description
Quod Libet is a GTK+-based audio player written in Python. It's designed
around the idea that you know better than we do how to organize your music.
It lets you make playlists based on regular expressions (don't worry,
regular searches work too). It lets you display and edit any tags you want
in the file.

It supports Ogg Vorbis and MP3 by default, but other formats (FLAC, Musepack,
Wavepack, MPEG-4/AAC and MOD are available through gstreamer0.10 plugins.

Quod Libet easily scales to libraries of thousands of songs. It also supports
most of the features you expect from a modern media player, like Unicode
support, gapless playback, multimedia keys, and an OSD. 

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/quodlibet/plugins/
cp -rf editing %{buildroot}/%{_datadir}/quodlibet/plugins/
cp -rf events %{buildroot}/%{_datadir}/quodlibet/plugins/
cp -rf songsmenu %{buildroot}/%{_datadir}/quodlibet/plugins/
cp %{SOURCE1} %{buildroot}%{_datadir}/quodlibet/plugins/songsmenu
cp %{SOURCE2} %{buildroot}%{_datadir}/quodlibet/plugins/

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# quodlibet plugins directory
QL_PLD=/usr/share/quodlibet/plugins

# we want to provide a clean upgrade path from previous versions
PYC_FILES=`find ${QL_PLD} -name "*.pyc"`
# don't touch .pyc files that are created by the quodlibet package
PYC_FILES=`echo ${PYC_FILES} | sed -e s,${QL_PLD}/editing.pyc,,`
PYC_FILES=`echo ${PYC_FILES} | sed -e s,${QL_PLD}/events.pyc,,`
PYC_FILES=`echo ${PYC_FILES} | sed -e s,${QL_PLD}/__init__.pyc,,`
PYC_FILES=`echo ${PYC_FILES} | sed -e s,${QL_PLD}/songsmenu.pyc,,`

for i in ${PYC_FILES}
do
    rm $i
done

%files
%defattr(0644,root,root,0755)
%{_datadir}/quodlibet/plugins/
%{_datadir}/quodlibet/plugins/
%{_datadir}/quodlibet/plugins/
