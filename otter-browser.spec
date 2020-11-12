%define oname otter
Name:		otter-browser
Summary:	Web browser controlled by the user, not vice-versa
License:	GPLv3
Version:	1.0.01
Release:	5
Group:		Networking/WWW 
URL:		http://otter-browser.org/
Source0:	https://github.com/OtterBrowser/otter-browser/archive/v%{version}/%{name}-%{version}.tar.gz
# mirror https://sourceforge.net/projects/otter-browser/files/otter-browser-%{version}/%{name}-%{version}.tar.bz2
#Patch to fix https://issues.openmandriva.org/show_bug.cgi?id=2550
Patch0: otter-browser-start-page-fix-openmandriva.patch
Patch1: https://patch-diff.githubusercontent.com/raw/OtterBrowser/otter-browser/pull/1640.patch

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
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.2
BuildRequires:  pkgconfig(Qt5Qml) >= 5.2
BuildRequires:  pkgconfig(Qt5Svg) >= 5.2
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5XmlPatterns) >= 5.2
BuildRequires:	desktop-file-utils
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(hunspell)

%description
Browser aiming to recreate classic Opera (12.x) UI using Qt5.


%prep
%setup -q
%patch0 -p0
%patch1 -p1

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
