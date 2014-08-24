%define oname otter
Name:		otter-browser
Summary:	Web browser controlled by the user, not vice-versa
License:	GPLv3
Version:	0.9.02
Release:	1
Group:		Networking/WWW 
URL:		http://otter-browser.org/
Source:		https://github.com/Emdek/%{oname}/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2
BuildRequires:  pkgconfig(Qt5Sensors) >= 5.2
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKit) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.2
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:	desktop-file-utils
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Concurrent)

%description
Browser aiming to recreate classic Opera (12.x) UI using Qt5.


%prep
%setup -qn %{oname}-%{version}


%build
%cmake_qt5
%make


%install
%makeinstall_std -C build

%files
%doc CHANGELOG README.md COPYING TODO HACKING
%{_bindir}/otter-browser
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}.png