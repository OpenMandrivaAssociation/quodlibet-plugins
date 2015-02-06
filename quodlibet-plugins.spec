Name: 	 	quodlibet-plugins
Summary: 	Advanced, elegant jukebox style music player plugins
Epoch:		1
Version: 	2.4.1
Release: 	2

Source0:	%{name}-%{version}.tar.gz
URL:		http://code.google.com/p/quodlibet/
License:	GPLv2
Group:		Sound
BuildArch:	noarch

BuildRequires:	python
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
mkdir -p %{buildroot}%{py_sitedir}/quodlibet/plugins
cp -rf * %{buildroot}%{py_sitedir}/quodlibet/plugins/


%files
%defattr(0644,root,root,0755)
%{py_sitedir}/quodlibet/plugins/*
