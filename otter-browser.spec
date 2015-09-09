%define oname otter
%define _appdatadir %{_datadir}/appdata

Name:		otter-browser
Summary:	Web browser controlled by the user, not vice-versa
License:	GPLv3
Version:	0.9.07
Release:	1
Group:		Networking/WWW 
URL:		http://otter-browser.org/
Source:		https://github.com/Emdek/%{oname}/archive/v%{version}.tar.gz

BuildRequires:  cmake >= 2.8.10.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2
BuildRequires:  pkgconfig(Qt5Sensors) >= 5.2
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKit) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.2
BuildRequires:  pkgconfig(Qt5Script) >= 5.2
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.2
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Concurrent) >= 5.2
BuildRequires:	pkgconfig(Qt5DBus) >= 5.2
BuildRequires:	pkgconfig(Qt5WebEngine) >= 5.2
BuildRequires:	qt5-qtbase-devel >= 5.2
BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils

%description
Browser aiming to recreate classic Opera (12.x) UI using Qt5.


%prep
%setup -q

%build
%cmake_qt5
%make


%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_appdatadir}
cp -R packaging/%{name}.appdata.xml \
  %{buildroot}%{_appdatadir}/%{name}.appdata.xml

%{find_lang} %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_appdatadir}/*.xml

%files -f %{name}.lang
%doc CHANGELOG README.md COPYING TODO 
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_appdatadir}/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/otter-browser.1.*


