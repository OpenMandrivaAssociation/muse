%define name	muse
%define version	0.8.1
%define	release	%mkrel 3

#%define __libtoolize /bin/true

Name:		%{name}
Summary:	MusE is a MIDI/Audio sequencer with recording and editing capabilities
Version:	%{version}
Release:	%{release}
URL:		http://lmuse.sourceforge.net/
Source:		%{name}-%{version}a.tar.bz2
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	jackit-devel libalsa-devel openjade doxygen qt3-devel
BuildRequires:  fluidsynth-devel libsndfile-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	docbook-style-dsssl docbook-dtd41-sgml
BuildRequires:	ladcca-devel >= 0.4.0
License:	GPL

%description
MusE is a MIDI/Audio sequencer with recording and editing capabilities
written by Werner Schweer.  MusE aims to be a complete multitrack virtual
studio for Linux, it is published under the GNU General Public License.
MusE has among other things support for:
    * Midi sequencing
    * Audio sequencing
    * LADSPA
    * Jack
    * ALSA - based on the Advanced Linux Sound Architecture 

You can use several soundcards to access external midi devices and
record/playback them with MusE. 

*NOTE: To use muse, you must enable the realtime-lsm kernel module (2.6 kernel
       only) or change /usr/bin/muse to suid root (chmod 4755).  You must
       also have jackd running as the same user.
       
%prep
%setup -q
#perl -p -i -e 's/spinboxfp/spinboxFP/g' muse/widgets/itransformbase.cpp muse/widgets/itransformbase.ui

%build
%configure2_5x --disable-optimize --with-docbook-stylesheets=/usr/share/sgml/docbook/dsssl-stylesheets-1.79 --disable-qttest --disable-suid-install --disable-suid-build --enable-ladcca --with-qt-libraries=/usr/lib/qt3/%_lib
%make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT SUIDINSTALL=no install

mkdir -p $RPM_BUILD_ROOT%_menudir
# (mandrake) menu support
cat << EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}): longtitle="MIDI sequencer" \
command="%{_bindir}/%{name}" title="MusE"  needs="x11" \
section="Multimedia/Sound" \
icon="sound_section.png" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=MusE
Comment=MIDI sequencer
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Midi;
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc INSTALL ChangeLog README* SECURITY
%_bindir/*
%_libdir/%name
%_datadir/%name
%_menudir/*
%{_datadir}/applications/mandriva-%{name}.desktop


