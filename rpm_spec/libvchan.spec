#
# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2010  Joanna Rutkowska <joanna@invisiblethingslab.com>
# Copyright (C) 2010  Rafal Wojtczuk  <rafal@invisiblethingslab.com>
# Copyright (C) 2012  Marek Marczykowski <marmarek@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#

%{!?version: %define version %(cat version)}

Name:		qubes-libvchan-xen
Version:	%{version}
Release:	1%{dist}

Summary:	Qubes vchan libraries
License:	GPL v2 only
Group:		Qubes
Vendor:		Invisible Things Lab
URL:		http://www.qubes-os.org
Obsoletes:  qubes-core-libs < 2.1.2
Provides:   qubes-core-libs
Provides:   qubes-libvchan
BuildRequires: xen-devel >= 4.2

%define _builddir %(pwd)

%description
The Qubes core libraries for installation inside a Qubes Dom0 and VM.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build
(cd u2mfn; make)
(cd vchan; make -f Makefile.linux)

%install
install -D -m 0644 vchan/libvchan.h $RPM_BUILD_ROOT%{_includedir}/vchan-xen/libvchan.h
install -D -m 0644 u2mfn/u2mfnlib.h $RPM_BUILD_ROOT%{_includedir}/u2mfnlib.h
install -D -m 0644 u2mfn/u2mfn-kernel.h $RPM_BUILD_ROOT%{_includedir}/u2mfn-kernel.h
install -D -m 0644 vchan/vchan-xen.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/vchan-xen.pc

install -D vchan/libvchan-xen.so $RPM_BUILD_ROOT/%{_libdir}/libvchan-xen.so
install -D u2mfn/libu2mfn.so $RPM_BUILD_ROOT/%{_libdir}/libu2mfn.so

%clean
rm -rf $RPM_BUILD_ROOT
rm -f %{name}-%{version}

%files
%{_libdir}/libvchan-xen.so
%{_libdir}/libu2mfn.so

%package devel
Summary:        Include files for qubes core libraries
License:        GPL v2 only
Group:          Development/Sources 
Obsoletes:      qubes-core-appvm-devel
Obsoletes:      qubes-core-vm-devel < 2.1.2
Obsoletes:      qubes-core-libs-devel < 2.1.2
Provides:      qubes-core-vm-devel
Provides:       qubes-core-libs-devel
Provides:       qubes-libvchan-devel
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel

%files devel
%{_includedir}/vchan-xen/libvchan.h
%{_libdir}/pkgconfig/vchan-xen.pc
%{_includedir}/u2mfnlib.h
%{_includedir}/u2mfn-kernel.h
