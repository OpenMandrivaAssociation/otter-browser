%define oname otter
Name:		otter-browser
Summary:	Web browser controlled by the user, not vice-versa
License:	GPLv3
Version:	0.9.96
Release:	1
Group:		Networking/WWW 
URL:		http://otter-browser.org/
Source0:	https://github.com/Emdek/%{oname}/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:	ninja
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2
BuildRequires:  pkgconfig(Qt5Sensors) >= 5.2
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKit) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.2
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.2
BuildRequires:	desktop-file-utils
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Concurrent)

%description
Browser aiming to recreate classic Opera (12.x) UI using Qt5.


%prep
%setup -q


%build
%cmake_qt5 -G Ninja
%ninja


%install
%ninja_install -C build

%{find_lang} %{name} --with-qt

%files -f %{name}.lang
%doc CHANGELOG README.md COPYING TODO
%{_bindir}/otter-browser
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}.png
%{_mandir}/man1/otter-browser.1*
%lang(jbo) %{_datadir}/otter-browser/locale/otter-browser_jbo.qm
%lang(yue) %{_datadir}/otter-browser/locale/otter-browser_yue.qm
