Summary:	NES/SNES style RPG
Summary(pl.UTF-8):	Gra RPG rodem z NES/SNES
Name:		monster
Version:	1.23
Release:	1
License:	BSD
Group:		X11/Applications/Games
Source0:	http://www.nooskewl.com/monster/Monster-%{version}-src.tar.gz
# Source0-md5:	1976726b4c453c0e3b33f591d7c1293d
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-util.patch
Patch1:		%{name}-lua.patch
Patch2:		%{name}-Makefile.patch
URL:		http://www.nooskewl.com/
BuildRequires:	allegro-devel >= 4.2.1
BuildRequires:	freetype-devel
BuildRequires:	fudgefont-devel >= 1.2
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	logg-devel >= 2.5
BuildRequires:	lua51-devel
BuildRequires:	tgui-devel >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monster is a short NES/SNES style RPG.

%description -l pl.UTF-8
Monster jest krótką grą RPG rodem z NES/SNES.

%prep
%setup -q -n Monster-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} -f Makefile.unix \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install src/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -r data $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
